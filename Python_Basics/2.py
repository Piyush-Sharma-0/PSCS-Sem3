lst = [12, 15, 20, 22, 24]
mean = sum(lst) / len(lst)
variance=0
for i in lst:
    variance += (i - mean) ** 2
variance=variance/len(lst)
std_dev = variance ** 0.5
print("Variance=",variance)
print("Standard Deviantion=",std_dev)
