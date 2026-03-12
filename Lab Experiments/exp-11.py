import numpy as np

fuel_efficiency = np.array([18, 22, 25, 28, 30, 35, 40, 32, 27, 24])

average_efficiency = np.mean(fuel_efficiency)

old_model_index = 2
new_model_index = 6

old_model_efficiency = fuel_efficiency[old_model_index]
new_model_efficiency = fuel_efficiency[new_model_index]

percentage_improvement = ((new_model_efficiency - old_model_efficiency) / old_model_efficiency) * 100

print("Fuel Efficiency Data (MPG):", fuel_efficiency)
print("Average Fuel Efficiency:", average_efficiency)
print("Old Model Efficiency:", old_model_efficiency)
print("New Model Efficiency:", new_model_efficiency)
print("Percentage Improvement:", percentage_improvement, "%")
