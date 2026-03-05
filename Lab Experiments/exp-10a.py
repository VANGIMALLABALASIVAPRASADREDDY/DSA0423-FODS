import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

temperature = [22,24,27,30,34,36,35,34,32,29,26,23]

plt.plot(months, temperature, marker='o')

plt.title("Monthly Temperature Data")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")

plt.show()
