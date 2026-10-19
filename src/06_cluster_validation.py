from pathlib import Path
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

project_dir = Path(__file__).resolve().parent.parent

gene_expression_selected = pd.read_csv(project_dir / "data"/ "processed"/ "gene_expression_2000.csv", index_col="SAMPLE_ID")
print(gene_expression_selected.shape)


## PCA n=20
##=====================================

pca= PCA(n_components=20, svd_solver="full")
pca_results = pca.fit_transform(gene_expression_selected)
print("\nPCA Shape", pca_results.shape)


## K-means check random seed
##======================================

from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

cluster_orig = KMeans(n_clusters=2, random_state=67, n_init=10).fit_predict(pca_results)

cluster_new = KMeans(n_clusters=2, random_state=42, n_init=10).fit_predict(pca_results)

ari= adjusted_rand_score(cluster_orig,cluster_new)
print("\nAdjusted score", round(ari,4))

# Multiple 

for seed in [10, 20, 30, 50, 100]:
    new_clusters = KMeans(n_clusters=2,random_state=seed,n_init=10).fit_predict(pca_results)

    ari = adjusted_rand_score(cluster_orig, new_clusters)

    print(f"Seed {seed}: ARI = {ari:.4f}")


## Change in PCA
##================================

for n in [10,20,30]:
    pca_test = PCA(n_components=n, svd_solver="full")
    pca_test_result = pca_test.fit_transform(gene_expression_selected)

    new_clusters2 = KMeans(n_clusters=2, random_state=67, n_init=10).fit_predict(pca_test_result)

    ari = adjusted_rand_score(cluster_orig, new_clusters2)
    print(f"{n} components: ARI = {ari:.4f}")

## Clustering is not highly sensitive to the number of PCA components


## Check against saved cluster
##==================================

saved_clusters = pd.read_csv(project_dir / "data"/ "processed"/ "patient_clusters.csv", index_col="SAMPLE_ID")
saved_clusters = saved_clusters.loc[gene_expression_selected.index]

ari_saved = adjusted_rand_score(saved_clusters["Cluster"], cluster_orig)
print("ARI vs original cluster", round(ari_saved, 4))

## Check patient clusters
##=================================

from sklearn.metrics import confusion_matrix
print(confusion_matrix(saved_clusters["Cluster"], cluster_orig))

## Conclusion: Our two-cluster solution is highly stable under the tested settings.