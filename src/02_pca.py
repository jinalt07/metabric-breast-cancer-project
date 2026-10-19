from pathlib import Path
import pandas as pd
from sklearn.decomposition import PCA

project_dir = Path(__file__).resolve().parent.parent

gene_expression_selected = pd.read_csv(project_dir / "data" / "processed" / "gene_expression_2000.csv", index_col="SAMPLE_ID")

##==============================================
## PCA (n=2)
##==============================================

pca = PCA(n_components=2)
pca_result = pca.fit_transform(gene_expression_selected)

print("Shape", gene_expression_selected.shape)
print("PCA shape", pca_result.shape)
print("Variance explaination", pca.explained_variance_ratio_)

## Visualize PCA
##==============================================

import matplotlib.pyplot as plt

plt.figure(figsize=(9,6))

plt.scatter(pca_result[:,0], pca_result[:,1], alpha=0.5, s=15)

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA of Breast Cancer Gene Expression")

plt.tight_layout
#plt.show()


##=================================================
## PCA (n=20)
##================================================

pca_20 = PCA(n_components=20)
pca_20.fit(gene_expression_selected)

print("Variance 20PC", pca_20.explained_variance_ratio_.sum())
print("Variance 10PC", pca_20.explained_variance_ratio_[:10].sum())

## Visualize PCA n=20

import numpy as np

cumulative_variance = np.cumsum(pca_20.explained_variance_ratio_)

plt.figure(figsize=(9,6))

plt.plot (range(1,21), cumulative_variance *100)

plt.xlabel("No. of PCs")
plt.ylabel("Cumulative Explained Var %")
plt.title("PCA Cumulative Explained Variance")

plt.grid(True)
plt.tight_layout()

plt.savefig(project_dir / "output" / "figures" / "pca_cumulative_variance.png", dpi= 300, bbox_inches = "tight")
plt.show()
