ages = [19, 22, 25, 30, 21, 24, 20, 18, 28, 27]
ages.sort()
total_values = len(ages)
cdf_list = []

for i in range(total_values):
    x = ages[i]
    cumulative_prob = (i + 1) / total_values
    cdf_list.append((x, cumulative_prob))

print("Age\tCDF")
for x, prob in cdf_list:
    print(f"{x}\t{prob}")
