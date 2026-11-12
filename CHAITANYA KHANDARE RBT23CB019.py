import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [1, 2],
    [2, 3],
    [3, 2],
    [8, 8],
    [9, 8],
    [8, 9],
    [15, 2],
    [16, 3],
    [15, 4],
    [12,2],
    [13 ,3],

])

def calculate_distance(data):
    n = len(data)
    distance = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            distance[i, j] = np.linalg.norm(data[i] - data[j])

    return distance

dist = calculate_distance(data)

medoids = [0, 3, 6]
k = 3

def calculate_cost(medoids, dist):
    return np.sum(np.min(dist[:, medoids], axis=1))

# 4. Apply PAM swapping algorithm
improved = True

while improved:
    improved = False
    current_cost = calculate_cost(medoids, dist)

    for m in range(k):
        for candidate in range(len(data)):
            if candidate not in medoids:
                new_medoids = medoids.copy()
                new_medoids[m] = candidate

                new_cost = calculate_cost(new_medoids, dist)

                if new_cost < current_cost:
                    medoids = new_medoids
                    current_cost = new_cost
                    improved = True
                    break

        if improved:
            break


labels = np.argmin(dist[:, medoids], axis=1)

print("Original Dataset:")
print(data)

print("\nCluster Assignments:")
for i in range(len(data)):
    print(f"Point {data[i]} -> Cluster {labels[i]}")

final_medoids = data[medoids]

print("\nFinal Medoids:")
print(final_medoids)

print("\nTotal Clustering Cost:")
print(round(calculate_cost(medoids, dist), 2))

plt.figure(figsize=(8, 6))

for cluster in range(k):
    points = data[labels == cluster]
    plt.scatter(
        points[:, 0],
        points[:, 1],
        label=f"Cluster {cluster}"
    )

plt.scatter(
    final_medoids[:, 0],
    final_medoids[:, 1],
    c="red",
    marker="X",
    s=250,
    label="Medoids"
)

plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("K-Medoids Clustering Using PAM")
plt.legend()
plt.grid(True)
plt.show()