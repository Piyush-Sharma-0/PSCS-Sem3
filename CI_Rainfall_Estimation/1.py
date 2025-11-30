import numpy as np
import matplotlib.pyplot as plt

n = 50
population_mean = 10
population_sd = 3

rainfall = np.random.normal(population_mean, population_sd, n)

sample_mean = sum(rainfall) / n
variance=0
for x in rainfall:
    variance += ((x - sample_mean)**2)
variance/= n - 1
sample_sd = variance**0.5

z = 1.96
error = z * (sample_sd / (n**0.5))
lower_bound = sample_mean - error
upper_bound = sample_mean + error

print("Sample Mean:", round(sample_mean, 3))
print("Sample SD:", round(sample_sd, 3))
print(f"95% CI: ({round(lower_bound, 3)}, {round(upper_bound, 3)})")


plt.figure(figsize=(8,5))
plt.hist(rainfall, bins=10, color="lightblue", edgecolor="black")

# Add mean line
plt.axvline(sample_mean, color='red', linestyle='-', linewidth=2, 
            label=f"Mean = {round(sample_mean, 2)}")

# Add CI boundary lines
plt.axvline(lower_bound, color='green', linestyle='--', linewidth=2, 
            label=f"Lower CI = {round(lower_bound, 2)}")
plt.axvline(upper_bound, color='green', linestyle='--', linewidth=2, 
            label=f"Upper CI = {round(upper_bound, 2)}")

# Add labels and title
plt.xlabel("Daily Rainfall (mm)")
plt.ylabel("Frequency")
plt.title("Histogram of Simulated Daily Rainfall (50 Days)")
plt.legend()
plt.show()


intervals = []
contains_true_mean = []

for _ in range(100):
    sample = np.random.normal(population_mean, population_sd, n)
    sample_mean = sum(sample) / n
    variance = 0
    for x in sample:
        variance += ((x - sample_mean)**2)
    variance /= (n - 1)
    sample_sd = variance**0.5

    margin = z * (sample_sd / (n**0.5))
    lower = sample_mean - margin
    upper = sample_mean + margin

    intervals.append((lower, upper))
    contains_true_mean.append(lower <= population_mean <= upper)

count = sum(contains_true_mean)

plt.figure(figsize=(8, 10))

for i, ((lower, upper), contains) in enumerate(zip(intervals, contains_true_mean)):
    color = "blue" if contains else "red"
    plt.hlines(y=i, xmin=lower, xmax=upper, color=color, linewidth=2)

plt.axvline(population_mean, color='black', linestyle='--', linewidth=2, label="True Mean = 10 mm")

plt.xlabel("Confidence Interval Range")
plt.ylabel("Sample Number (1 to 100)")
plt.title("100 Confidence Intervals for Daily Rainfall Mean (95% CI)")
plt.legend()
plt.show()

print(f"Number of intervals containing the true mean: {count} out of {len(intervals)}")