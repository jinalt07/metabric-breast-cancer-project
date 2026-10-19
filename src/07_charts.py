from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

project_dir = Path(__file__).resolve().parent.parent

gene_expression_selected = pd.read_csv(project_dir / "data" / "processed" / "gene_expression_2000.csv",index_col="SAMPLE_ID")
clusters = pd.read_csv(project_dir / "data" / "processed" / "patient_clusters.csv",index_col="SAMPLE_ID")


## 1. PCA cluster charts
##=================================

pca= PCA(n_components=2)
pca_result = pca.fit_transform(gene_expression_selected)

plot_data = pd.DataFrame(pca_result, columns=["PC1", "PC2"], index=gene_expression_selected.index)
plot_data["Cluster"] = clusters["Cluster"]

plt.figure(figsize=(8,6))

cluster_0 = plot_data[plot_data["Cluster"] == 0]
cluster_1 = plot_data[plot_data["Cluster"] == 1]

plt.scatter(cluster_0["PC1"], cluster_0["PC2"], label = "Cluster 0", alpha=0.6, s=15)
plt.scatter(cluster_1["PC1"], cluster_1["PC2"], label= "Cluster 1", alpha= 0.6, s=15)
plt.xlabel("PC1 (14.94% variance)")
plt.ylabel("PC2 (8.34% variance)")
plt.title("METABRIC Breast Cancer Patient Clusters")
plt.legend()
plt.savefig(project_dir / "output" / "figures" / "pca_clusters.png", dpi=300)
#plt.show()


## 2. ER status chart
##=================================

er_percentage = pd.DataFrame({"ER positive": [97.81,21.73],
                              "ER negative": [2.19, 78.27]}, index=["Cluter 0", "Cluster 1"])
er_percentage.plot(kind="bar", figsize=(7,5))

plt.title("ER Status by Patient Cluster")
plt.xlabel("Patient Cluster")
plt.ylabel("Percentage of Patients (%)")
plt.xticks(rotation=0)
plt.legend(title="ER Status")
plt.tight_layout()
plt.savefig(project_dir / "output" / "figures" / "er_status_comparison.png", dpi=300)
plt.show()


## HER2 Chart
##==================================

her2_percentage = pd.DataFrame({"HER2 Positive": [7.57, 24.73],"HER2 Negative": [92.43, 75.27]}, index=["Cluster 0", "Cluster 1"])
her2_percentage.plot(kind="bar", figsize=(7, 5))

plt.title("HER2 Status by Patient Cluster")
plt.xlabel("Patient Cluster")
plt.ylabel("Percentage of Patients (%)")
plt.xticks(rotation=0)
plt.legend(title="HER2 Status")
plt.tight_layout()

plt.savefig(project_dir / "output" / "figures" / "her2_status_comparison.png",dpi=300)
plt.show()


## 4. Tumor Grade chart
##==================================

grade_percentage = pd.DataFrame({"Grade 1": [11.94, 1.47],"Grade 2": [50.89, 15.62],"Grade 3": [37.17, 82.90]}, index=["Cluster 0", "Cluster 1"])

grade_percentage.plot(kind="bar", figsize=(7, 5))

plt.title("Tumor Grade by Patient Cluster")
plt.xlabel("Patient Cluster")
plt.ylabel("Percentage of Patients (%)")
plt.xticks(rotation=0)
plt.legend(title="Tumor Grade")
plt.tight_layout()
plt.savefig(project_dir / "output" / "figures" / "tumor_grade_comparison.png",dpi=300)
plt.show()


## 5. Molecular Subtype chart
##=======================================

subtype_counts = pd.DataFrame({"Luminal A": [695, 5],"Luminal B": [449, 26],"Basal": [8, 201],"Claudin-low": [30, 188], "HER2-enriched": [106, 118],"Normal-like": [120, 28], "NC": [6, 0]}, index=["Cluster 0", "Cluster 1"])
subtype_percentage = subtype_counts.div(subtype_counts.sum(axis=1), axis=0) * 100
subtype_percentage.plot( kind="bar",stacked=True,figsize=(9, 6))

plt.title("Molecular Subtype Distribution by Patient Cluster")
plt.xlabel("Patient Cluster")
plt.ylabel("Percentage of Patients (%)")
plt.xticks(rotation=0)
plt.legend(title="Molecular Subtype", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()


plt.savefig(project_dir / "output" / "figures" / "molecular_subtype_comparison.png",dpi=300)
plt.show()


## 6. Gene Expression chart
##=====================================

gene_data = pd.read_csv(project_dir / "output" / "gene_expression_differences.csv")
genes = ["ESR1", "FOXA1", "GATA3", "S100A8", "S100A9", "GABRP"]
selected_genes = gene_data[gene_data["Gene"].isin(genes)]

plt.figure(figsize=(8, 5))

plt.barh(selected_genes["Gene"],selected_genes["Mean_Difference"], color=selected_genes["Mean_Difference"].gt(0).map({ True: "steelblue",False: "coral"}))

plt.axvline(0, color="black", linewidth=1)
plt.xlabel("Mean Expression Difference (Cluster 0 - Cluster 1)")
plt.ylabel("Gene")
plt.title("Representative Gene Expression Differences")
plt.tight_layout()


plt.savefig(project_dir / "output" / "figures" / "gene_expression_comparison.png", dpi=300)
plt.show()