import numpy as np

# Prices of products sold in the past month
prices = np.array([120, 250, 300, 150, 200, 180, 220])

# Calculate average price
average_price = np.mean(prices)

print("PRODUCT PRICE DATA")
print("---------------------------")
print("Prices of Products:", prices)

print("\nANALYSIS RESULT")
print("---------------------------")
print("Average Price of Products Sold:", average_price)
