import random

arr = ["Q"+str(i) for i in range(1, 101)]
num_tests = 10000

# With replacement
q1_count_wr = 0
q1_q2_count_wr = 0

for _ in range(num_tests):
    test = [random.randint(1, 100) for _ in range(5)]
    if 1 in test:  # Q1 selected (Q1 corresponds to 1)
        q1_count_wr += 1
        if 2 in test:  # Q2 also selected
            q1_q2_count_wr += 1

cond_prob_wr = q1_q2_count_wr / q1_count_wr
print("With replacement: P(Q2 | Q1) =", cond_prob_wr)

# Without replacement
q1_count_wor = 0
q1_q2_count_wor = 0

for _ in range(num_tests):
    test = random.sample(range(1, 101), 5)  # 5 unique questions
    if 1 in test:
        q1_count_wor += 1
        if 2 in test:
            q1_q2_count_wor += 1

cond_prob_wor = q1_q2_count_wor / q1_count_wor
print("Without replacement: P(Q2 | Q1) =", cond_prob_wor)
