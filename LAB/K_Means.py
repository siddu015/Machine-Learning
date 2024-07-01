import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

data = np.random.rand(100, 2)
np.savetxt('data.csv', data, delimiter=',')

data = np.loadtxt('data.csv', delimiter=',')

kmeans = KMeans(n_clusters=3)
kmeans.fit(data)

labels = kmeans.labels_
centers = kmeans.cluster_centers_
silhouette = silhouette_score(data, labels)

print("Cluster labels:", labels)
print("Cluster centers:\n", centers)
print("Silhouette Score:", silhouette)
