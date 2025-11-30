import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

# ===============================
# 1. Load & clean dataset
# ===============================
df = pd.read_csv("adult.csv")

df = df[["capital.gain", "education", "income", "hours.per.week"]]
df = df.replace("?", np.nan).dropna()
df["capital.gain"] = pd.to_numeric(df["capital.gain"], errors="coerce").fillna(0)

edu_groups = df.groupby("education")
educations = sorted(df["education"].unique())

# Utility: create subplot grid
def create_grid(num_plots):
    cols = 3
    rows = math.ceil(num_plots / cols)
    return rows, cols


# ============================================
# 2. ALL RAW CAPITAL-GAIN HISTOGRAMS TOGETHER
# ============================================
rows, cols = create_grid(len(educations))
plt.figure(figsize=(15, rows * 4))

for i, edu in enumerate(educations, 1):
    group = df[df["education"] == edu]
    plt.subplot(rows, cols, i)
    plt.hist(group["capital.gain"], bins=40, alpha=0.7, color="steelblue")
    plt.title(f"{edu}")
    plt.xlabel("Capital Gain")
    plt.ylabel("Freq")

plt.suptitle("Raw Capital-Gain Distribution by Education Level", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


# ============================================
# 3. CLT SAMPLING FOR n = 5, 30, 100
# ============================================
sample_sizes = [5, 30, 100]
num_samples = 1000

for n in sample_sizes:

    rows, cols = create_grid(len(educations))
    plt.figure(figsize=(15, rows * 4))
    
    for i, edu in enumerate(educations, 1):
        group = df[df["education"] == edu]
        data = group["capital.gain"].values

        # Collect sample means
        sample_means = [np.random.choice(data, n, replace=True).mean() for _ in range(num_samples)]
        sample_means = np.array(sample_means)

        # Fit Normal PDF
        mean_hat = sample_means.mean()
        sd_hat = sample_means.std()
        x_vals = np.linspace(sample_means.min(), sample_means.max(), 200)
        pdf_vals = norm.pdf(x_vals, mean_hat, sd_hat)

        # Subplot
        plt.subplot(rows, cols, i)
        plt.hist(sample_means, bins=30, density=True, alpha=0.6, color="lightgreen", edgecolor="black")
        plt.plot(x_vals, pdf_vals)
        plt.title(f"{edu}")
        plt.xlabel("Sample Mean")
        plt.ylabel("Density")

    plt.suptitle(f"Sampling Distribution of Means (n = {n}) Across Education Groups", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()
