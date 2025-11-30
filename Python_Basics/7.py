rainfall = [2, 0, 5, 30, 45, 10, 3, 25, 0, 50]

for r in rainfall:
    if r == 0:
        category = "None"
    elif r > 0 and r <= 10:
        category = "Low"
    elif r > 10 and r <= 30:
        category = "Moderate"
    else:
        category = "Heavy"
    print(f"{r} mm: {category}")
