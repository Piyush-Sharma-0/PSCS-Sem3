import pandas as pd
import numpy as np
from scipy.stats import binom, norm

# Load dataset
df = pd.read_csv("website_wata.csv")

# ------------------ Task 1 ------------------
p = 0.2
n1 = 50
k1 = 10
prob_1 = binom.pmf(k1, n1, p)

# ------------------ Task 2 ------------------
n2 = 50
k2 = 25
prob_2 = 1 - binom.cdf(k2 - 1, n2, p)

# ------------------ Task 3 ------------------
threshold = np.percentile(df["Bounce Rate"], 10)
most_engaged = df[df["Bounce Rate"] <= threshold]
percent_engaged = (len(most_engaged) / len(df)) * 100

# ------------------ Task 4 ------------------
conv_rate_engaged = most_engaged["Conversion Rate"].mean()
remaining = df[df["Bounce Rate"] > threshold]
conv_rate_remaining = remaining["Conversion Rate"].mean()

# ------------------ Task 5 ------------------
n5 = 200
p5 = 0.2
mean = n5 * p5
sd = np.sqrt(n5 * p5 * (1 - p5))
z = (50.5 - mean) / sd
prob_5 = 1 - norm.cdf(z)

# ------------------ Output ------------------
print("Probability of exactly 10 conversions out of 50 (p=0.2):", round(prob_1, 4))
print("Probability of at least 25 conversions out of 50 Organic sessions:", round(prob_2, 4))
print("Percentage of sessions in most engaged (lowest 10% bounce rate):", round(percent_engaged, 2))
print("Conversion rate among most engaged visitors:", round(conv_rate_engaged, 4))
print("Conversion rate among remaining 90% visitors:", round(conv_rate_remaining, 4))
print("Normal approx probability that >50 conversions occur out of 200 sessions:", round(prob_5, 4))
