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

mean_duration = np.mean(all_durations)
variance_duration = np.var(all_durations)

print("Empirical mean of ride durations =", round(mean_duration, 2))
print("Empirical variance of ride durations =", round(variance_duration, 2))