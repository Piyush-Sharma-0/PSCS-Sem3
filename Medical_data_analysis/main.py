import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D

# ================================
# Load dataset (your format)
# ================================
df = pd.read_csv("diabetes.csv")

# Columns where zeros = missing
missing_cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

# Small noise variance sigma_small^2
sigma_small = 0.1     # small fixed std deviation for imputation noise

rng = np.random.default_rng(42)
df_clean = df.copy()

# =========================================
# 1. Mean-imputation with small random noise
# =========================================
for col in missing_cols:
    values = df_clean[col].values.astype(float)
    mask = values == 0
    non_zero_values = values[~mask]

    if len(non_zero_values) == 0:
        continue

    mu = non_zero_values.mean()
    noise = rng.normal(0, sigma_small, mask.sum())
    values[mask] = mu + noise
    df_clean[col] = values


# =====================================================
# 2. BIVARIATE NORMAL ANALYSIS (Glucose, BMI)
# =====================================================
X = df_clean["Glucose"].values
Y = df_clean["BMI"].values
data = np.column_stack([X, Y])

# (a) Mean vector and covariance matrix
mean_vec = data.mean(axis=0)
cov_mat = np.cov(data.T)

# Multivariate normal distribution
rv = multivariate_normal(mean=mean_vec, cov=cov_mat)

# ================================
# 2(b) Scatter + bivariate contours
# ================================
x_range = np.linspace(X.min() - 5, X.max() + 5, 200)
y_range = np.linspace(Y.min() - 5, Y.max() + 5, 200)
Xgrid, Ygrid = np.meshgrid(x_range, y_range)
pos = np.dstack((Xgrid, Ygrid))
Z = rv.pdf(pos)

plt.figure(figsize=(8, 6))
plt.scatter(X, Y, s=10, alpha=0.4)
CS = plt.contour(Xgrid, Ygrid, Z, levels=7)
plt.clabel(CS, inline=True, fontsize=8)
plt.scatter(mean_vec[0], mean_vec[1], c='red', s=50)
plt.xlabel("Glucose")
plt.ylabel("BMI")
plt.title("Bivariate Normal Fit: Glucose vs BMI (Scatter + Contours)")
plt.show()

# ================================
# 2(c) 3D surface plot
# ================================
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(Xgrid, Ygrid, Z, cmap="viridis", alpha=0.8)
ax.scatter(mean_vec[0], mean_vec[1], rv.pdf(mean_vec), c='red', s=50)
ax.set_xlabel("Glucose")
ax.set_ylabel("BMI")
ax.set_zlabel("PDF")
ax.set_title("Bivariate Normal PDF Surface")
plt.show()


# =========================================================
# 3. CONDITIONAL PROBABILITY OF DIABETES GIVEN (x, y)
# =========================================================

# Separate class 0 and 1
df0 = df_clean[df_clean["Outcome"] == 0]
df1 = df_clean[df_clean["Outcome"] == 1]

X0 = df0[["Glucose", "BMI"]].values
X1 = df1[["Glucose", "BMI"]].values

pi0 = len(df0) / len(df_clean)
pi1 = len(df1) / len(df_clean)

mu0 = X0.mean(axis=0)
cov0 = np.cov(X0.T)
mu1 = X1.mean(axis=0)
cov1 = np.cov(X1.T)

rv0 = multivariate_normal(mean=mu0, cov=cov0)
rv1 = multivariate_normal(mean=mu1, cov=cov1)

# Conditional probability P(Outcome=1 | x, y)
def diabetes_prob(x, y):
    p0 = rv0.pdf([x, y])
    p1 = rv1.pdf([x, y])
    return (pi1 * p1) / (pi0 * p0 + pi1 * p1)


# ============================================
# 3(b) HEATMAP OF DIABETES RISK OVER GRID
# ============================================
x_vals = np.linspace(X.min(), X.max(), 200)
y_vals = np.linspace(Y.min(), Y.max(), 200)

Xg, Yg = np.meshgrid(x_vals, y_vals)
ProbGrid = np.zeros_like(Xg)

for i in range(Xg.shape[0]):
    for j in range(Xg.shape[1]):
        ProbGrid[i, j] = diabetes_prob(Xg[i, j], Yg[i, j])

plt.figure(figsize=(8, 6))
plt.imshow(
    ProbGrid,
    origin="lower",
    extent=[x_vals.min(), x_vals.max(), y_vals.min(), y_vals.max()],
    aspect="auto",
    cmap="RdBu_r"
)
plt.colorbar(label="P(Outcome = 1)")
plt.xlabel("Glucose")
plt.ylabel("BMI")
plt.title("Diabetes Risk Heatmap (Red = high risk)")

# contour lines: 0.2, 0.5, 0.8
CS = plt.contour(Xg, Yg, ProbGrid, levels=[0.2, 0.5, 0.8], colors=["yellow", "white", "black"])
plt.clabel(CS, inline=True, fontsize=8)

plt.show()
