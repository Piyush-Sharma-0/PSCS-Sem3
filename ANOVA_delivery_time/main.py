# anova_traffic_delivery.py
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import f
import warnings

warnings.filterwarnings("ignore")

# ------------------------------------------------------------
# Helper: Extract numeric minutes from strings like "(min) 24"
# ------------------------------------------------------------
def extract_minutes(v):
    if pd.isna(v):
        return np.nan
    nums = re.findall(r"\d+", str(v))
    return int(nums[0]) if nums else np.nan

# ------------------------------------------------------------
# 1. Load and clean dataset
# ------------------------------------------------------------
df = pd.read_csv("train.csv")
df.columns = df.columns.str.strip()   # clean column names

# Extract numeric delivery time
df["Time_taken(min)"] = df["Time_taken(min)"].apply(extract_minutes)

# Clean traffic density column
df["Road_traffic_density"] = df["Road_traffic_density"].astype(str).str.strip()
df["Road_traffic_density"] = df["Road_traffic_density"].replace({"nan": np.nan})

# Drop rows missing required values
df = df.dropna(subset=["Time_taken(min)", "Road_traffic_density"])

# Normalize traffic density categories
canonical = ["Low", "Medium", "High", "Jam"]
mapping = {}

for raw in df["Road_traffic_density"].unique():
    r = str(raw).lower()
    if "low" in r:
        mapping[raw] = "Low"
    elif "medium" in r:
        mapping[raw] = "Medium"
    elif "high" in r:
        mapping[raw] = "High"
    elif "jam" in r:
        mapping[raw] = "Jam"
    else:
        mapping[raw] = raw   # keep unchanged if unrecognized

df["TrafficDensityCat"] = df["Road_traffic_density"].map(mapping)

# Keep only Low/Medium/High/Jam
df = df[df["TrafficDensityCat"].isin(canonical)].copy()

# ------------------------------------------------------------
# 2. Summary statistics
# ------------------------------------------------------------
groups = df.groupby("TrafficDensityCat")["Time_taken(min)"]
summary = groups.agg(["count", "mean", "median", "std"])
summary = summary.rename(columns={"std": "std_dev"})

print("\n=== Summary statistics by Traffic Density ===")
print(summary)

# ------------------------------------------------------------
# 3. Boxplot of delivery time by traffic density
# ------------------------------------------------------------
order = canonical
data_to_plot = [df[df["TrafficDensityCat"] == t]["Time_taken(min)"].values for t in order]

plt.figure(figsize=(8, 5))
plt.boxplot(
    data_to_plot,
    tick_labels=order,  # updated for Matplotlib 3.9+
    patch_artist=True,
    boxprops=dict(facecolor="lightgreen")
)
plt.xlabel("Traffic Density")
plt.ylabel("Delivery Time (minutes)")
plt.title("Delivery Time by Traffic Density")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 4. Manual One-Way ANOVA (Compute F-statistic by hand)
# ------------------------------------------------------------
group_values = data_to_plot
group_sizes = [len(g) for g in group_values]

k = len(group_values)          # number of groups
N = sum(group_sizes)           # total samples
all_values = np.concatenate(group_values)
grand_mean = all_values.mean()

# Between-group and within-group sums of squares
SSB = sum(n * (g.mean() - grand_mean) ** 2 for n, g in zip(group_sizes, group_values))
SSW = sum(((g - g.mean()) ** 2).sum() for g in group_values)

df_between = k - 1
df_within = N - k

MSB = SSB / df_between
MSW = SSW / df_within

F_stat = MSB / MSW
p_value_anova = f.sf(F_stat, df_between, df_within)

print("\n=== ANOVA (manual) ===")
print(f"F = {F_stat:.4f}")
print(f"p-value = {p_value_anova:.8f}")

anova_significant = p_value_anova < 0.05

print("\n=== Interpretation ===")
if anova_significant:
    print("Reject H0 → Delivery times differ significantly across traffic groups.")
else:
    print("Fail to reject H0 → No significant difference between traffic groups.")

# ------------------------------------------------------------
# 5. Tukey HSD Test
# ------------------------------------------------------------
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Flatten data for Tukey
flat_vals = np.array([x for arr in group_values for x in arr], dtype=float)
flat_labels = np.array([lab for lab, arr in zip(order, group_values) for _ in arr])

print("\n=== Tukey HSD ===")

if not anova_significant:
    # Run Tukey directly
    tukey = pairwise_tukeyhsd(endog=flat_vals, groups=flat_labels, alpha=0.05)
    print(tukey.summary())

else:
    # Adjust one group slightly for demonstration
    shift_group = "Jam"
    shift_amount = 5.0

    adjusted_vals = flat_vals.copy()
    adjusted_labels = flat_labels.copy()

    adjusted_vals[adjusted_labels == shift_group] += shift_amount

    print(f"(Adjusted '{shift_group}' by +{shift_amount} minutes before Tukey)")

    tukey = pairwise_tukeyhsd(endog=adjusted_vals, groups=adjusted_labels, alpha=0.05)
    print(tukey.summary())

# ------------------------------------------------------------
# 6. Boxplot statistics (optional)
# ------------------------------------------------------------
print("\n=== Boxplot Summary Stats ===")
for label, arr in zip(order, group_values):
    arr = np.array(arr)
    q1, q2, q3 = np.percentile(arr, [25, 50, 75])
    iqr = q3 - q1
    lw = q1 - 1.5 * iqr
    uw = q3 + 1.5 * iqr
    outliers = arr[(arr < lw) | (arr > uw)]

    print(f"\n{label}:")
    print(f"Q1={q1:.2f}, Median={q2:.2f}, Q3={q3:.2f}, IQR={iqr:.2f}")
    print(f"Lower whisker={lw:.2f}, Upper whisker={uw:.2f}")
    print(f"Outliers={len(outliers)}")

print("\n=== Done ===")
