from pathlib import Path
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

project_dir = Path(__file__).resolve().parent.parent


gene_expression_selected = pd.read_csv(project_dir / "data" / "processed" / "gene_expression_2000.csv",index_col="SAMPLE_ID")

pca = PCA(n_components=20)
pca_result = pca.fit_transform(gene_expression_selected)

kmeans = KMeans(n_clusters=3, random_state= 67, n_init=10)
clusters = kmeans.fit_predict(pca_result)

print("\nNo. of patients", len(clusters))
print("Cluster size")
print(pd.Series(clusters).value_counts().sort_index())

print("\nSilhouette score", silhouette_score(pca_result,clusters))


for k in range(2, 7):
    kmeans = KMeans(n_clusters=k, random_state=67, n_init=10)

    clusters = kmeans.fit_predict(pca_result)

    score = silhouette_score(pca_result, clusters)

    print(f"k={k}, Silhouette score={score:.4f}")

## k = 2

kmeans = KMeans(n_clusters=2, random_state=67, n_init=10)
clusters = kmeans.fit_predict(pca_result)

print("Cluster sizes:")
print(pd.Series(clusters).value_counts().sort_index())

## Visualize

import matplotlib.pyplot as plt

plt.figure(figsize=(9, 6))

plt.scatter(pca_result[:, 0],pca_result[:, 1],c=clusters,cmap="coolwarm",alpha=0.6, s=15)

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("K-means Clustering of METABRIC Patients (k=2)")
plt.colorbar(label="Cluster")
plt.tight_layout()
plt.show()


cluster_results = pd.DataFrame({"SAMPLE_ID": gene_expression_selected.index,"Cluster": clusters})

cluster_results.to_csv(project_dir / "data" / "processed" / "patient_clusters.csv",index=False)

print(cluster_results.head())