import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

rainfall = [10,15,20,35,60,120,150,140,100,60,25,15]

plt.scatter(months, rainfall)

plt.title("Monthly Rainfall Data")
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")

plt.show()
