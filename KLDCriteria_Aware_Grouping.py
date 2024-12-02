import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# Path to the dataset, it should be balanced dataset obtained from the KLD-aware stage.
url = "database name.csv"
# Add necessary QIDs, please add required QIDs.
column_names = ["age", "workclass",  "education", "sex", "income"]
data = pd.read_csv(url, header=None, names=column_names, na_values=" ?", skipinitialspace=True)
# This step is optional as data is already clean. It can also be omitted
data.dropna(inplace=True)
# Separate QIDs & SA.
X = data.drop(columns=['income'])
encoder = OneHotEncoder(drop='first', sparse_output=False)
X_encoded = encoder.fit_transform(X)
# Standardize the data (to accelerate clustering and computing similarity values)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)
#Apply K-means Clustering based on similarity
k = 200  # Specify k-anonymity criteria. Change this value as per the experimental testing.
n_clusters = len(data) // k  # Computing the total # of clusters.
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X_scaled)
labels = kmeans.labels_
# Add cluster labels to the original data
data['Cluster'] = labels
# Ensure max diversity == 2-Diversity as we deal with binary dataset.
def ensure_2diversity_and_min_size(data, min_size):
    cluster_sizes = data['Cluster'].value_counts()
    # List of clusters to merge that fail to accomplish KLD criteria.
    clusters_to_merge = []
    for cluster, size in cluster_sizes.items():
        if size < min_size:
            clusters_to_merge.append(cluster)
        # This value should be changed as per SA value in each dataset.
        income_counts = data[data['Cluster'] == cluster]['income'].value_counts()
        if len(income_counts) == 1:  
            clusters_to_merge.append(cluster)
    for cluster in clusters_to_merge:
        # Find the largest cluster to merge with based on closeness.
        largest_cluster = cluster_sizes.idxmax()
        data.loc[data['Cluster'] == cluster, 'Cluster'] = largest_cluster
    return data

# Guarantee 2-diversity & minimum cluster size (e.g., k-anonymity criteria)
data = ensure_2diversity_and_min_size(data, k)
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X_scaled)
labels = kmeans.labels_
data['Cluster'] = labels
all_cluster_data = []
for cluster_num in range(n_clusters):  
    cluster_data = data[data['Cluster'] == cluster_num]
    all_cluster_data.append(cluster_data)
    final_cluster_data = pd.concat(all_cluster_data, ignore_index=True)
    output_file = 'clustered_databaseName_data.csv'
    final_cluster_data.to_csv(output_file, index=False)

