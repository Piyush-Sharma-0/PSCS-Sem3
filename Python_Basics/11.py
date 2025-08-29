import random
import matplotlib.pyplot as plt

def estimate_pi(trials):
    inside_x = []
    inside_y = []
    outside_x = []
    outside_y = []

    in_points = 0
    for _ in range(trials):
        x = random.uniform(0.0, 1.0)
        y = random.uniform(0.0, 1.0)
        if (x**2 + y**2) <= 1:
            in_points += 1
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)

    pi = 4 * in_points / trials
    return pi, inside_x, inside_y, outside_x, outside_y

trials = 5000
pi, inside_x, inside_y, outside_x, outside_y = estimate_pi(trials)

print(f"Estimated Pi: {pi}")

plt.figure(figsize=(6, 6))
plt.scatter(inside_x, inside_y, color="blue", s=5, label="Inside Circle")
plt.scatter(outside_x, outside_y, color="red", s=5, label="Outside Circle")

circle = plt.Circle((0, 0), 1, fill=False, color="black", linewidth=2)
plt.gca().add_artist(circle)

plt.title("Monte Carlo Simulation of π")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.axis("equal")
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()
