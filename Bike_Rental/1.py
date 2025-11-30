import random
import numpy as np
import pandas as pd

#(a)Random assignment

rentals_random = [random.randint(0, 15) for _ in range(24)]
ride_durations_random = []
for r in rentals_random:
    ride_durations_random.append([random.randint(5, 60) for _ in range(r)])

#print("Random rentals per hour:", rentals_random)
#print("Random ride durations:", ride_durations_random)

#(b)Statistical simulation

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

rentals_poisson = [np.random.poisson(rentals) for rentals in means]
ride_durations_exp = []
for i in range(len(rentals_poisson)):
    temp=[]
    for j in range(rentals_poisson[i]):
        x=(np.random.exponential(scale=30))
        temp.append(round(x,0))
    ride_durations_exp.append(temp)
#print("Poisson rentals per hour:", rentals_poisson)
#print("Exponential ride durations:", ride_durations_exp)

# (c)CSV entry
df = pd.read_csv("bike_data.csv")

ride_durations_csv = []
for r in df['Rentals']:
    ride_durations_csv.append([random.randint(5, 60) for _ in range(r)])

#print("CSV rentals per hour:", list(df['Rentals']))
#print("CSV ride durations per hour:", ride_durations_csv)
