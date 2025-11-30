import random
import numpy as np
import matplotlib.pyplot as plt

num_tests = 10000
num_questions = 100
questions_per_test = 5

# Initialize co-occurrence matrix
co_matrix = np.zeros((num_questions, num_questions), dtype=int)

# Simulate tests with replacement
for _ in range(num_tests):
    test = [random.randint(0, num_questions-1) for _ in range(questions_per_test)]
    # Count co-occurrences
    for i in range(questions_per_test):
        for j in range(questions_per_test):
            co_matrix[test[i], test[j]] += 1

# Plot heatmap
plt.figure(figsize=(10, 8))
plt.imshow(co_matrix, cmap='hot', interpolation='nearest')
plt.colorbar(label="Co-selection frequency")
plt.title("Heatmap of Question Co-selection Frequencies (10,000 tests)")
plt.xlabel("Question Index")
plt.ylabel("Question Index")
plt.show()
