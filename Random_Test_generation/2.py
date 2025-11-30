import random

arr = ["Q"+str(i) for i in range(1, 101)]

def selection_with_replacement(count):
    selection = []
    for _ in range(5):
        x = random.randint(1, 100)
        selection.append("Q"+str(x))
        count[x-1] += 1
    return selection, count

def selection_without_replacement(count):
    selection = []
    while len(selection) < 5:
        x = random.randint(1, 100)
        if x in [int(q[1:]) for q in selection]:
            continue
        else:
            selection.append("Q"+str(x))
            count[x-1] += 1
    return selection, count

def simulate_test_with_replacement():
    test_count = [0]*100
    for _ in range(10000):
        _, test_count = selection_with_replacement(test_count)
    return test_count

def simulate_test_without_replacement():
    test_count = [0]*100
    for _ in range(10000):
        _, test_count = selection_without_replacement(test_count)
    return test_count

# Run simulations
count_with_replacement = simulate_test_with_replacement()
count_without_replacement = simulate_test_without_replacement()

print("Counts with replacement:", count_with_replacement)
print("Counts without replacement:", count_without_replacement)
