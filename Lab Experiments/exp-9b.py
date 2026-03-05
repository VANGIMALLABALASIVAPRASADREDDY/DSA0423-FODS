import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun"]
sales = [2000,2500,3000,2800,3500,4000]

plt.bar(months, sales)

plt.title("Monthly Sales Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales Amount")

plt.show()
