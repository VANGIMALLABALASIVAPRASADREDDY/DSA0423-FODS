import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    "CustomerID": [1,2,3,4,5,6,7,8,9,10],
    "TotalAmountSpent": [200, 1500, 300, 2500, 800, 1200, 100, 2200, 700, 1600],
    "ItemsPurchased": [5, 40, 8, 60, 20, 35, 3, 55, 18, 45]
}

df = pd.DataFrame(data)

X = df[["TotalAmountSpent", "ItemsPurchased"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X_scaled)

plt.figure()
plt.scatter(df["TotalAmountSpent"], df["ItemsPurchased"])
centers = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centers[:,0], centers[:,1])
plt.xlabel("Total Amount Spent")
plt.ylabel("Items Purchased")
plt.title("Customer Segmentation using K-Means")
plt.show()

print(df)
