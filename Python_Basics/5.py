records = [('pass', 60), ('fail', 30), ('absent', 0), ('pass', 85), ('fail', 40), ('absent', 0)]
count_fail_or_absent = 0

for status, marks in records:
    if status == 'fail' or status == 'absent':
        count_fail_or_absent += 1

total_students = len(records)
probability = count_fail_or_absent / total_students

print("Number of students failed or absent:", count_fail_or_absent)
print("P(fail or absent) =", probability)
