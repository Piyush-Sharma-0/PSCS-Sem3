scores = [85, 72, 90, 66, 58, 45, 38, 93, 77, 50]
grade_counts = {'A': 0, 'B': 0, 'C': 0, 'F': 0}

for score in scores:
    if score >= 80:
        grade_counts['A'] += 1
    elif score >= 60:
        grade_counts['B'] += 1
    elif score >= 40:
        grade_counts['C'] += 1
    else:
        grade_counts['F'] += 1

total_students = len(scores)

for grade in grade_counts:
    probability = grade_counts[grade] / total_students
    print("P(",grade,")=",probability)
