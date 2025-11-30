import numpy as np
import matplotlib.pyplot as plt

num_questions = 100
questions_per_test = 5
num_tests = 10000

# Define probability weights
weights = np.ones(num_questions)
weights[:20] = 5  # Q1–Q20 are 5 times more likely
probabilities = weights / weights.sum()  # Normalize to sum=1

# Count selection frequencies
counts = np.zeros(num_questions)

for _ in range(num_tests):
    test = np.random.choice(np.arange(1, num_questions+1), size=questions_per_test, replace=True, p=probabilities)
    for q in test:
        counts[q-1] += 1

# Plot histogram
plt.figure(figsize=(12,6))
plt.bar(np.arange(1, num_questions+1), counts)
plt.xlabel("Question Number")
plt.ylabel("Sel")
