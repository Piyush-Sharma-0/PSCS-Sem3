import random
import numpy as np

num_days = 10000
hours_per_day = 24

all_rentals = [] 
all_durations = []    

for _ in range(num_days):
    rentals_day = [random.randint(0, 15) for _ in range(hours_per_day)]
    all_rentals.append(rentals_day)
    
    for r in rentals_day:
        durations = [random.randint(5, 60) for _ in range(r)]
        all_durations.extend(durations)

all_rentals = np.array(all_rentals)
all_durations = np.array(all_durations)
# (a) Probability rentals > 10 in a randomly chosen hour

prob_more_than_10 = np.sum(all_rentals > 10) / (num_days * hours_per_day)
print("P(rentals > 10 in an hour) =", round(prob_more_than_10,2))

# (b) Hour with maximum rentals in the first day

first_day = all_rentals[0]
hour_max = np.argmax(first_day)
print("Hour with maximum rentals=",hour_max)

# (c) Empirical probability of observing that maximum value over 10,000 days

max_value = first_day[hour_max]
prob_max_value = np.sum(all_rentals == max_value) / (num_days * hours_per_day)
print("Empirical P(observing max value)=", prob_max_value)

# (d) Probability a ride lasted more than 30 minutes

prob_duration_gt_30 = np.sum(all_durations > 30) / len(all_durations)
print("P(ride > 30 minutes)=", prob_duration_gt_30)

# (e) Probability a ride lasted between 20 and 25 minutes

prob_duration_20_25 = np.sum((all_durations >= 20) & (all_durations <= 25)) / len(all_durations)
print("P(ride between 20 and 25 minutes)=", prob_duration_20_25)
