import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun"]
sales = [2000,2500,3000,2800,3500,4000]

plt.plot(months, sales, marker='o')

plt.title("Monthly Sales Line Plot")
plt.xlabel("Months")
plt.ylabel("Sales Amount")

plt.grid(True)

plt.show()
