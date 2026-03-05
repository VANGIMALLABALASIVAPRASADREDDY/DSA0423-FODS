import numpy as np

house_data = np.array([
[3,1200,200000],
[5,2500,450000],
[4,1800,300000],
[6,3000,600000]
])

bedrooms = house_data[:,0]
prices = house_data[:,2]

selected_prices = prices[bedrooms > 4]

average_price = np.mean(selected_prices)

print("Prices of houses with bedrooms > 4 :",selected_prices)
print("Average Sale Price :",average_price)
