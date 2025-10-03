# Elevate Labs - Task 8: K-Means Clustering

### **Objective**
The primary objective was to apply the **K-Means Clustering** algorithm to segment mall customers based on their Annual Income and Spending Score. The key focus was on determining the optimal number of clusters (K) and interpreting the resulting segments.

### **Workflow & Key Steps**

1.  **Data Preparation**: The `Annual Income` and `Spending Score` features were extracted. **Feature Scaling (StandardScaler)** was applied to both features, which is essential for K-Means to ensure accurate distance calculation.
2.  **Optimal K Determination**: The **Elbow Method** was executed by plotting the Within-Cluster Sum of Squares (WCSS) against K (from 1 to 10).
3.  **Elbow Finding**: The elbow in the WCSS plot was observed at **K=[Insert Optimal K Value]**, which was selected as the optimal number of segments.
4.  **K-Means Application**: The `KMeans` algorithm was applied to the scaled data using the optimal K.

### **Cluster Interpretation (Customer Segmentation)**

The resulting [Insert Optimal K Value] clusters represent distinct customer segments. Based on the visualization, here are the typical segments found:

| Segment | Annual Income (k$) | Spending Score (1-100) | Interpretation |
| :--- | :--- | :--- | :--- |
| **Cluster 1** | Low | High | **The "Spenders"**: Low income, but high spending. Highly engaged and potentially impulsive buyers. |
| **Cluster 2** | High | Low | **The "Careful"**: High income, but low spending. Potential to be converted with high-value product offerings. |
| **Cluster 3** | High | High | **The "Target"**: High income and high spending. The most valuable segment for retention and loyalty programs. |
| **Cluster 4** | Low | Low | **The "Miser"**: Low income and low spending. Difficult to convert. |
| **Cluster 5** | Medium | Medium | **The "Average"**: Moderate income and spending. Represents the broad customer base. |

### **Conclusion**
The K-Means model successfully identified [Insert Optimal K Value] distinct, actionable customer segments. These insights are crucial for the mall's marketing team to create targeted campaigns and optimize resource allocation.
