import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# --- 1. Load and Prepare the Data ---
df = pd.read_csv('Mall_Customers.csv')

# Select the two key features for clustering (X)
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Scaling is critical for K-Means!
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("Data preparation complete (Features Scaled).\n")

# --- 2. Elbow Method: Finding the Optimal K ---
wcss = [] # Within-Cluster Sum of Squares (Inertia)
max_k = 11

for i in range(1, max_k):
    # n_init='auto' is the modern standard for KMeans
    kmeans = KMeans(n_clusters=i, init='k-means++', n_init='auto', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plotting the Elbow Method
plt.figure(figsize=(10, 6))
plt.plot(range(1, max_k), wcss, marker='o', linestyle='--', color='blue')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS (Inertia)')
plt.grid(True)
plt.show() 

# --- 3. Apply K-Means with Optimal K ---
# Visually determine the "elbow" point from the plot. A common result is K=5.
optimal_k = 5 
print(f"\nApplying K-Means with Optimal K = {optimal_k}...")

final_kmeans = KMeans(n_clusters=optimal_k, init='k-means++', n_init='auto', random_state=42)
# Fit the model and get the cluster labels
y_kmeans = final_kmeans.fit_predict(X_scaled)

# Add the cluster labels back to the original (unscaled) DataFrame for visualization
df['Cluster'] = y_kmeans

# --- 4. Visualize the Final Clusters ---
plt.figure(figsize=(10, 8))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', 
                data=df, palette='viridis', s=100)

# Plot the centroids (converted back to the original scale for interpretation)
centroids_scaled = final_kmeans.cluster_centers_
centroids_original = scaler.inverse_transform(centroids_scaled)

plt.scatter(centroids_original[:, 0], centroids_original[:, 1], 
            s=300, c='red', marker='X', label='Centroids')

plt.title(f'Customer Segments using K-Means (K={optimal_k})')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

print("\nK-Means clustering and visualization complete.")
