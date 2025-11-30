import numpy as np
from scipy.stats import norm

# ------------------ Task 1 ------------------
mu1 = 5
sigma1 = 2
prob_1 = 1 - norm.cdf(8, mu1, sigma1)

# ------------------ Task 2 ------------------
mu2 = 3
sigma2 = 1.2
prob_2 = norm.cdf(4.5, mu2, sigma2) - norm.cdf(2, mu2, sigma2)

# ------------------ Task 3 ------------------
mu3 = 4
sigma3 = 1.5
n3 = 30
se3 = sigma3 / np.sqrt(n3)
prob_3 = 1 - norm.cdf(5, mu3, se3)

# ------------------ Task 4 ------------------
mu_org = 5.2
sigma_org = 1.8
mu_paid = 4.7
sigma_paid = 2.0

# Difference distribution: Organic − Paid
mu_diff = mu_org - mu_paid
sigma_diff = np.sqrt(sigma_org**2 + sigma_paid**2)
prob_4 = 1 - norm.cdf(0, mu_diff, sigma_diff)

# ------------------ Task 5 ------------------
mu5 = 3
sigma5 = 1.5
prob_5 = 1 - norm.cdf(5, mu5, sigma5)

# ------------------ Task 6 ------------------
mu6 = 5
sigma6 = 2
n6 = 40
se6 = sigma6 / np.sqrt(n6)
prob_6 = norm.cdf(4.5, mu6, se6)

# ------------------ Output ------------------
print("Probability session lasts more than 8 minutes:", round(prob_1, 4))
print("Probability time on page is between 2 and 4.5 minutes:", round(prob_2, 4))
print("Probability sample mean pages viewed > 5 (n=30):", round(prob_3, 4))
print("Probability Organic session lasts longer than Paid session:", round(prob_4, 4))
print("Probability visitor has at least 5 previous visits:", round(prob_5, 4))
print("Probability sample mean session duration < 4.5 minutes (n=40):", round(prob_6, 4))
