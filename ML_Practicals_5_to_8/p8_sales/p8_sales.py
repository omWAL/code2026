import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.cluster.hierarchy import linkage, dendrogram

df = pd.read_csv("sales_data_sample.csv")
cols = ["QUANTITYORDERED", "PRICEEACH", "SALES"]
X = StandardScaler().fit_transform(df[cols])      # scale the data

# Elbow method: find inertia (error) for k = 1 to 8
inertia = []
for k in range(1, 9):
    inertia.append(KMeans(n_clusters=k, n_init=10, random_state=1).fit(X).inertia_)
    print("k =", k, " inertia =", round(inertia[-1], 2))
plt.plot(range(1, 9), inertia, marker="o")
plt.title("Elbow Method"); plt.xlabel("Number of clusters (k)"); plt.ylabel("Inertia")
plt.show()

# K-Means with the k seen at the elbow
km = KMeans(n_clusters=3, n_init=10, random_state=1)
df["Cluster"] = km.fit_predict(X)
print("\nOrders in each cluster:\n", df["Cluster"].value_counts().sort_index())
print("\nAverage values per cluster:\n", df.groupby("Cluster")[cols].mean().round(1))

# Hierarchical clustering (dendrogram + clusters)
dendrogram(linkage(X, method="ward"))
plt.title("Dendrogram"); plt.show()
df["HC_Cluster"] = AgglomerativeClustering(n_clusters=3).fit_predict(X)
print("\nHierarchical cluster sizes:\n", df["HC_Cluster"].value_counts().sort_index())
