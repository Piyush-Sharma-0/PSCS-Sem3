import random

arr = ["Q"+str(i) for i in range(1, 101)]

def simulate_unique_with_replacement(num_tests=10000):
    unique_counts = []
    for _ in range(num_tests):
        test = [random.randint(1, 100) for _ in range(5)]
        unique_counts.append(len(set(test)))
    return sum(unique_counts)/num_tests

def simulate_unique_without_replacement(num_tests=10000):
    # Each test has 5 unique questions by design
    return 5

# Simulated results
avg_unique_with_replacement = simulate_unique_with_replacement()
avg_unique_without_replacement = simulate_unique_without_replacement()

# Theoretical result
theoretical_unique_with_replacement = 100*(1 - (99/100)**5)
theoretical_unique_without_replacement = 5

print("With replacement: simulated =", avg_unique_with_replacement,
      ", theoretical =", theoretical_unique_with_replacement)
print("Without replacement: simulated =", avg_unique_without_replacement,
      ", theoretical =", theoretical_unique_without_replacement)
