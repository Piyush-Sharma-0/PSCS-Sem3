tickets = [2, 3, 2, 4, 3, 3, 1, 2, 4, 4, 2, 2, 1, 3, 4]
pmf = {}
total_observations = len(tickets)

for k in range(1, 5):
    count = 0
    for t in tickets:
        if t == k:
            count += 1
    pmf[k] = count / total_observations

for k in pmf:
    print(f"P(X={k}) = {pmf[k]}")
