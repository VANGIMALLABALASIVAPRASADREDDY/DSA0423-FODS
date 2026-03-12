from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data=[[200,5],[500,8],[100,2],[600,9]]

k=KMeans(n_clusters=2)
k.fit(data)

labels=k.labels_

plt.scatter([i[0] for i in data],[i[1] for i in data],c=labels)
plt.show()
