# ROMIJUL LASKAR
# 20CS8065
import numpy as np
# Input supply, demand, and cost matrix
supply = np.array(input("Enter supply for factories (separated by spaces): ").split(), dtype=int)
demand = np.array(input("Enter demand for distribution centers (separated by spaces): ").split(), dtype=int)

num_factories = len(supply)
num_distribution_centers = len(demand)

cost_matrix = []
print("Enter the cost matrix:")
for _ in range(num_factories):
    row = list(map(int, input().split()))
    cost_matrix.append(row)
cost_matrix = np.array(cost_matrix)

allocation_matrix = np.zeros((num_factories, num_distribution_centers))
unallocated_factories = set(range(num_factories))
unallocated_centers = set(range(num_distribution_centers))

while unallocated_factories and unallocated_centers:
    penalties_factories = []
    for factory_idx in range(num_factories):
        row = cost_matrix[factory_idx]
        min1, min2 = np.partition(row, 2)[0:2]
        penalties_factories.append(min2 - min1)
        
    penalties_centers = []
    for center_idx in range(num_distribution_centers):
        col = cost_matrix[:, center_idx]
        min1, min2 = np.partition(col, 2)[0:2]
        penalties_centers.append(min2 - min1)

    max_penalty_factory_idx = np.argmax(penalties_factories)
    max_penalty_center_idx = np.argmax(penalties_centers)

    if penalties_factories[max_penalty_factory_idx] > penalties_centers[max_penalty_center_idx]:
        selected_factory = max_penalty_factory_idx
        selected_center = np.argmin(cost_matrix[selected_factory])
    else:
        selected_center = max_penalty_center_idx
        selected_factory = np.argmin(cost_matrix[:, selected_center])

    allocation = min(supply[selected_factory], demand[selected_center])
    allocation_matrix[selected_factory, selected_center] = allocation
    supply[selected_factory] -= allocation
    demand[selected_center] -= allocation

    if supply[selected_factory] == 0:
        unallocated_factories.remove(selected_factory)
    if demand[selected_center] == 0:
        unallocated_centers.discard(selected_center)

total_cost = np.sum(allocation_matrix * cost_matrix)
print("ROMIJUL LASKAR 20CS8065")
print("Allocation Matrix:")
print(allocation_matrix)
print("Total Transportation Cost:", total_cost)
