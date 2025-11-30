import random

arr = ["Q" + str(i) for i in range(1, 101)]

def selection_with_replacement(count):
    selection = []
    for _ in range(5):
        x = random.randint(1, 100)
        selection.append("Q" + str(x))
        count[x-1] += 1
    return selection, count

def selection_without_replacement(count):
    selection = []
    while len(selection) < 5:
        x = random.randint(1, 100)
        if x in [int(q[1:]) for q in selection]:
            continue
        else:
            selection.append("Q" + str(x))
            count[x-1] += 1
    return selection, count

# Initialize count lists
count1 = [0]*100
count2 = [0]*100

# Perform selections
s1, c1 = selection_with_replacement(count1)
s2, c2 = selection_without_replacement(count2)

# Print results
print("Selection with replacement:", s1)
print("Counts after selection:", c1)
print("Selection without replacement:", s2)
print("Counts after selection:", c2)
