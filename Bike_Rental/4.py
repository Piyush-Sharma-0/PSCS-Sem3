import random
import matplotlib.pyplot as plt
import numpy as np  # Only for convenience in calculating mean

num_days = 1000
hours_per_day = 24

all_rentals = []
all_durations = []

means = [0]*24
for i in range(24):
    if i<=6 or i>=21:
        means[i]=2
    elif i<=9:
        means[i]=12
    elif i<=15:
        means[i]=5
    else:
        means[i]=15

for _ in range(num_days):
    rentals_poisson = [np.random.poisson(rentals) for rentals in means]
    all_rentals.append(rentals_poisson)
    
    for r in rentals_poisson:
        temp = []
        for j in range(r):
            x = np.random.exponential(scale=30)
            temp.append(round(x, 0))
        all_durations.extend(temp)   # extend with numbers, not with list of lists


first_day = all_rentals[0]
average_rentals = [sum(hour)/num_days for hour in zip(*all_rentals)]  

# (a) Bar chart for first day
colors_first_day = ['red' if r > 10 else 'blue' for r in first_day]
plt.figure(figsize=(12,6))
plt.bar(range(24), first_day, color=colors_first_day)
plt.xlabel("Hour")
plt.ylabel("Number of Rentals")
plt.title("Number of Rentals in First Day (Red > 10)")
plt.show()

# (b) Bar chart for average rentals
colors_avg = ['red' if r > 10 else 'blue' for r in average_rentals]
plt.figure(figsize=(12,6))
plt.bar(range(24), average_rentals, color=colors_avg)
plt.xlabel("Hour")
plt.ylabel("Average Number of Rentals")
plt.title("Average Rentals Across 10,000 Days (Red > 10)")
plt.show()

# (c) Line graph for random day
random_day_index = random.randint(0, num_days-1)
random_day_rentals = all_rentals[random_day_index]
plt.figure(figsize=(12,6))
plt.plot(range(24), random_day_rentals, marker='o', linestyle='-')
plt.xlabel("Hour")
plt.ylabel("Number of Rentals")
plt.title("Rental Trend Over a Random Day")
plt.grid(True)
plt.show()

# (d) Frequency of each rental count on random day
freq_dict = {}
for r in random_day_rentals:
    freq_dict[r] = freq_dict.get(r, 0) + 1

plt.figure(figsize=(12,6))
plt.bar(freq_dict.keys(), freq_dict.values(), color='green')
plt.xlabel("Number of Rentals")
plt.ylabel("Frequency")
plt.title("Frequency of Each Rental Count on Random Day")
plt.show()

# (e) Histogram of all ride durations with mean line
plt.figure(figsize=(12,6))
plt.hist(all_durations, bins=30, color='purple', edgecolor='black', alpha=0.7)
mean_duration = np.mean(all_durations)
plt.axvline(mean_duration, color='red', linestyle='dashed', linewidth=2, label=f"Mean = {mean_duration:.1f}")
plt.xlabel("Ride Duration (minutes)")
plt.ylabel("Frequency")
plt.title("Histogram of Ride Durations Across 10,000 Days")
plt.legend()
plt.show()

# (f) Smoothed version of the histogram
plt.figure(figsize=(12,6))
counts, bins, _ = plt.hist(all_durations, bins=30, density=True, alpha=0.4, color='skyblue', edgecolor='black')

# Compute bin centers
bin_centers = 0.5 * (bins[1:] + bins[:-1])

# Overlay a smooth line (using the histogram values)
plt.plot(bin_centers, counts, color='red', linewidth=2, label="Smoothed curve")

plt.xlabel("Ride Duration (minutes)")
plt.ylabel("Density")
plt.title("Smoothed Histogram of Ride Durations")
plt.legend()
plt.show()

# (g) Highlight rides lasting more than 30 minutes
plt.figure(figsize=(12,6))
plt.hist(all_durations, bins=30, color='lightgreen', edgecolor='black', alpha=0.7)

# Threshold line
plt.axvline(30, color='red', linestyle='dashed', linewidth=2, label="30 min threshold")

# Shade region > 30
plt.axvspan(30, 120, color='orange', alpha=0.3, label="Rides >30 min")  
plt.xlim(0, 120)

plt.xlabel("Ride Duration (minutes)")
plt.ylabel("Frequency")
plt.title("Ride Durations with Highlight for >30 minutes")
plt.legend()
plt.show()

