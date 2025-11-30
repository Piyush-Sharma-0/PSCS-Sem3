import random
import matplotlib.pyplot as plt

num_tests = 10000
tests_per_group = 1000
num_groups = 10

# Simulate all tests with replacement
all_tests = []
for _ in range(num_tests):
    test = [random.randint(1, 100) for _ in range(5)]
    all_tests.append(test)

# Split into 10 groups and compute average distinct questions
avg_distinct_per_group = []
for i in range(num_groups):
    group_tests = all_tests[i*tests_per_group:(i+1)*tests_per_group]
    distinct_counts = [len(set(test)) for test in group_tests]
    avg_distinct = sum(distinct_counts) / len(distinct_counts)
    avg_distinct_per_group.append(avg_distinct)

# Create boxplot
plt.boxplot(avg_distinct_per_group)
plt.xlabel("Group")
plt.ylabel("Average number of distinct questions")
plt.title("Boxplot of Average Distinct Questions per Group")
plt.show()
