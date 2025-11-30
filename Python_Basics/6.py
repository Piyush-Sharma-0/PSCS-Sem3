times = [10, 12, 15, -1, 0, 20, 18, 25, -5, 30]
invalid_count = 0
valid_high_count = 0

for t in times:
    if not t > 0:
        invalid_count += 1
    elif t > 15 and t > 0:
        valid_high_count += 1

print("Invalid values count:", invalid_count)
print("Valid values greater than 15 count:", valid_high_count)
