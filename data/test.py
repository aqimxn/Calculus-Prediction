# Import necessary libraries
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Read the CSV file
file_path = 'cluster_data.csv'
df = pd.read_csv(file_path)

# Assuming the features you want to cluster are in all columns except the last one
X = df.iloc[:, :-1].values  # Adjust this if the structure of your CSV is different

# Perform Agglomerative Clustering with automatic cluster determination
agg_clust = AgglomerativeClustering(n_clusters=3)  # Set n_clusters to None and distance_threshold to 10
y_pred = agg_clust.fit_predict(X)

# Number of clusters determined by the algorithm
n_clusters_auto = len(set(y_pred))
print(f"Automatically determined number of clusters: {n_clusters_auto}")

# Add the cluster labels to the dataset
df['Cluster'] = y_pred

# Bubble chart plotting
plt.scatter(df.iloc[:, 0], df.iloc[:, 1], s=100, c=df['Cluster'], cmap='viridis', alpha=0.6)
plt.xlabel(df.columns[0])  # Assuming the first column is the x-axis
plt.ylabel(df.columns[1])  # Assuming the second column is the y-axis
plt.title(f"Agglomerative Clustering Results (Bubble Chart) - {n_clusters_auto} clusters")
plt.show()

# Generate Dendrogram
linked = linkage(X, 'ward')  # Perform hierarchical clustering with "ward" linkage

# Plot the dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked)

# Add a horizontal line to indicate the cutoff distance for clusters
plt.axhline(y=30, color='r', linestyle='--')  # Change the y-value to control the cutoff distance

plt.title("Dendrogram with Cutoff Line")
plt.xlabel("Sample index")
plt.ylabel("Distance")
plt.show()