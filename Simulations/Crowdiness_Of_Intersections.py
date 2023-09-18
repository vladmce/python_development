"""
This software alalyzes the efficience of an intersection with respect to the ratio between green and red lights
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
num_simulations = 1000  # Number of simulations for each ratio
ratios = np.linspace(0.1, 10, 10)  # Ratios from 0.1 to 10
intersection_capacity = 200  # Maximum number of vehicles the intersection can handle

# Simulate crowdiness for different ratios
crowdiness_factors = []

for ratio in ratios:
    total_waiting_time = 0

    for _ in range(num_simulations):
        cycle_duration = 100  # Fixed cycle duration for this simulation
        red_time = cycle_duration / (1 + ratio)
        green_time = cycle_duration - red_time

        # Generate random arrival times for vehicles (uniform distribution)
        arrival_times = np.sort(np.random.uniform(0, cycle_duration, intersection_capacity))

        # Calculate waiting times for vehicles at the intersection
        waiting_times = np.zeros(intersection_capacity)

        for i in range(1, intersection_capacity):
            if arrival_times[i] % cycle_duration <= red_time:
                waiting_times[i] = max(0, arrival_times[i - 1] + green_time - arrival_times[i])

        total_waiting_time += np.mean(waiting_times)

    # Calculate crowdiness factor as the average waiting time across simulations
    crowdiness_factor = total_waiting_time / num_simulations
    crowdiness_factors.append(crowdiness_factor)

# Plotting the results
sweet_spot_index = np.argmin(np.abs(ratios - 1))

plt.figure(figsize=(10, 6))
plt.plot(ratios, crowdiness_factors, marker='o', label='Crowdiness Factor')
plt.scatter(ratios[sweet_spot_index], crowdiness_factors[sweet_spot_index], color='green', s=300, label='Sweet Spot (Ratio 1)')
plt.xlabel('Red/Green Light Ratio')
plt.ylabel('Crowdiness Factor')
plt.title('Effect of Red/Green Light Ratio on Intersection Crowdiness')
plt.legend()
plt.grid()
plt.show()



