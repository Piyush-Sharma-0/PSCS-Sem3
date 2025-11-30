import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import re

# ==========================================================
# 1. LOAD & CLEAN THE DATA
# ==========================================================

# Load dataset
df = pd.read_csv("train.csv")
df.columns = df.columns.str.strip()

# ----------------------------------------------------------
# Convert "Time_taken(min)" from strings like "24 (min)" → 24
# ----------------------------------------------------------
def extract_minutes(x):
    if isinstance(x, str):
        nums = re.findall(r'\d+', x)      # extract digits
        return int(nums[0]) if nums else np.nan
    return x

df["Time_taken(min)"] = df["Time_taken(min)"].apply(extract_minutes)

# ----------------------------------------------------------
# Convert age to numeric (non-numeric entries become NaN)
# ----------------------------------------------------------
df["Delivery_person_Age"] = pd.to_numeric(df["Delivery_person_Age"], errors="coerce")

# Remove leading/trailing spaces from traffic density labels
df["Road_traffic_density"] = df["Road_traffic_density"].str.strip()

# ----------------------------------------------------------
# Drop rows where important fields are missing
# ----------------------------------------------------------
df = df.dropna(subset=["Time_taken(min)", "Delivery_person_Age", "Road_traffic_density"])


# ==========================================================
# 2. DRAW A RANDOM SAMPLE OF 100 DELIVERY TIMES
# ==========================================================

sample = df["Time_taken(min)"].sample(100, replace=True, random_state=42)

sample_mean = sample.mean()      # sample mean
sigma = 8                        # given population standard deviation
mu_claimed = 30                  # advertised delivery time


# ==========================================================
# 3. ONE-SAMPLE Z-TEST (Two-Tailed)
# ==========================================================

# Z-statistic formula:
# Z = (x̄ - μ) / (σ / √n)
z = (sample_mean - mu_claimed) / (sigma / np.sqrt(100))

# ----------------------------------------------------------
# p-value using standard normal survival function
# norm.sf(|z|) gives area in tail → multiply by 2 for two-tailed test
# ----------------------------------------------------------
p_value = norm.sf(abs(z)) * 2

print("Sample mean delivery time:", sample_mean)
print("Z-value:", z)
print("p-value:", p_value)


# ==========================================================
# 4. SCATTER PLOT: Delivery Person Age vs. Delivery Time
# ==========================================================

plt.figure(figsize=(7, 5))
plt.scatter(df["Delivery_person_Age"], df["Time_taken(min)"],
            alpha=0.5, color="steelblue")

plt.xlabel("Delivery Person Age")
plt.ylabel("Delivery Time (minutes)")
plt.title("Delivery Time vs Delivery Person Age")
plt.tight_layout()
plt.show()


# ==========================================================
# 5. BOXPLOT: Delivery Time by Traffic Density
# ==========================================================

# Specify display order
order = ["Low", "Medium", "High", "Jam"]

# Collect delivery times for each traffic level
data_to_plot = [
    df[df["Road_traffic_density"] == level]["Time_taken(min)"]
    for level in order
]

plt.figure(figsize=(8, 5))

# Create boxplot with custom colors
plt.boxplot(
    data_to_plot,
    tick_labels=order,
    patch_artist=True,
    boxprops=dict(facecolor="lightgreen")
)

plt.xlabel("Traffic Density")
plt.ylabel("Delivery Time (minutes)")
plt.title("Delivery Time Distribution Across Traffic Conditions")
plt.tight_layout()
plt.show()
