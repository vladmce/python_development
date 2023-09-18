import numpy as np
import matplotlib.pyplot as plt
import math


def simulate_collisions_optimized(Nsim, G, Rmax, radius, xmin, xmax, ymin, ymax, hmin, hmax):
    cmeanVector = []
    rateVector = []

    for N in G:
        collisions = np.random.rand(Nsim, N, 3)
        collisions[:, :, 0] = collisions[:, :, 0] * (xmax - xmin) + xmin
        collisions[:, :, 1] = collisions[:, :, 1] * (ymax - ymin) + ymin
        collisions[:, :, 2] = collisions[:, :, 2] * (hmax - hmin) + hmin

        distances = np.linalg.norm(collisions[:, np.newaxis, :, :] - collisions[:, :, np.newaxis, :], axis=-1)
        mask = np.triu(distances < 2 * radius, k=1)
        collisions_count = np.sum(mask, axis=(1, 2))

        cmean = collisions_count / (Nsim * N)
        R_col = (cmean / N) * 100

        cmeanVector.append(cmean)
        rateVector.append(R_col)

    return cmeanVector, rateVector


Nsim = 100
G = [10, 50, 100, 500, 1000]
Rmax = 200000  # 20 km in meters
radius = 3045  # meters

xmin = -Rmax
xmax = Rmax
ymin = -Rmax
ymax = Rmax
hmin = 30
hmax = 10000

cmeanVector, rateVector = simulate_collisions_optimized(Nsim, G, Rmax, radius, xmin, xmax, ymin, ymax, hmin, hmax)

# Plotting number of collisions
plt.figure(figsize=(10, 6))
plt.plot(G, cmeanVector, marker='o')
plt.xlabel('Number of Simulated Airplanes')
plt.ylabel('Number of Collisions')
plt.title('Number of Collisions vs. Number of Airplanes')
plt.grid()
plt.show()

# Plotting collision rate
plt.figure(figsize=(10, 6))
plt.plot(G, rateVector, marker='o', color='r')
plt.xlabel('Number of Simulated Airplanes')
plt.ylabel('Collision Rate (%)')
plt.title('Collision Rate vs. Number of Airplanes')
plt.grid()
plt.show()
