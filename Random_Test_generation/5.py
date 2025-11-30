import random

num_trials = 100000
easy_questions = list(range(30))   # indices 0-29
hard_questions = list(range(30, 100)) # indices 30-99

correct_and_easy = 0
total_correct = 0

for _ in range(num_trials):
    # select a random question
    q = random.randint(0, 99)
    
    # simulate correct answer
    if q in easy_questions:
        if random.random() < 0.9:
            total_correct += 1
            correct_and_easy += 1
    else:
        if random.random() < 0.4:
            total_correct += 1

# empirical P(Easy | Correct)
empirical_prob = correct_and_easy / total_correct
print("Empirical P(Easy | Correct) =", empirical_prob)

# theoretical probability
theoretical_prob = (0.9 * 0.3) / (0.9*0.3 + 0.4*0.7)
print("Theoretical P(Easy | Correct) =", theoretical_prob)
