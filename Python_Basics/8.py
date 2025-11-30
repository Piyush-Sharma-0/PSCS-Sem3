sessions = [('user1', 1), ('user2', 0), ('user3', 1), ('user4', 0), ('user5', 1)]
purchase_count = 0
total_sessions = 0

for user, purchase in sessions:
    total_sessions += 1
    if purchase == 1:
        purchase_count += 1

probability = purchase_count / total_sessions
print("Number of purchases:", purchase_count)
print("Total sessions:", total_sessions)
print("P(purchase | visited between 6pm and 9pm) =", probability)
