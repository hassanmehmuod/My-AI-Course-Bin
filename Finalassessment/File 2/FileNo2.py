import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv('D:\\Work\\Github\\My-AI-Course-Bin\\Finalassessment\\File 2\\Hospitals.csv')

print(df.shape)
print(df.columns.tolist())
print(df.head())
print(df.info())

df = df.drop(columns=['TTL_STAFF'])
df = df[df['BEDS'] != -999]
print("Shape after cleaning: ", df.shape)
print(df['BEDS'].describe())

features = df[['BEDS', 'LATITUDE','LONGITUDE']]

features = features.dropna()
df = df.loc[features.index]

print('Final shape for clustering: ', features.shape)

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
print(scaled_features[:5])


inertia = []
k_range = range(2, 11)

for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(scaled_features)
    inertia.append(km.inertia_)

plt.figure(figsize=(8,5))
plt.plot(k_range, inertia, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()

# Final KMeans model with k=4
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['CLUSTER'] = kmeans.fit_predict(scaled_features)

# Silhouette score - measures how well-separated the clusters are
sil_score = silhouette_score(scaled_features, df['CLUSTER'])
print("Silhouette Score:", sil_score)

# Cluster sizes
print(df['CLUSTER'].value_counts())

# Average BEDS per cluster - helps interpret what each cluster represents
print(df.groupby('CLUSTER')[['BEDS', 'LATITUDE', 'LONGITUDE']].mean())

plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='LONGITUDE', y='LATITUDE', hue='CLUSTER', palette='Set1', alpha=0.6)
plt.title('Hospital Clusters by Location and Size (k=4)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Bed count distribution per cluster
plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='CLUSTER', y='BEDS')
plt.title('Bed Count Distribution by Cluster')
plt.show()

print("For this task, I grouped hospitals using KMeans clustering based on two things: how many beds each hospital has, and its location (latitude and longitude). Before clustering, I cleaned the data by removing the TTL_STAFF column, since almost every value in it was missing, and by removing rows where BEDS was set to -999, which was just a placeholder for missing data. To decide how many groups (clusters) to use, I used the elbow method and found that 4 clusters worked best, since that's where the improvement started to level off. The clusters had a silhouette score of 0.355, meaning they were reasonably well separated, though not perfectly distinct. Looking at the results, three of the clusters represented small to medium-sized hospitals (around 95–120 beds), grouped roughly by US region — Midwest, West, and South. The fourth cluster stood out as a smaller group of much larger hospitals, averaging around 570 beds, and these were spread across different regions rather than being limited to one area. This likely represents major regional hospitals or medical centers. One limitation is that I only used bed count and location for clustering — including other details like hospital type or ownership might reveal more useful patterns.")