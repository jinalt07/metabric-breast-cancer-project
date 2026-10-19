from pathlib import Path
import pandas as pd

project_dir = Path(__file__).resolve().parent.parent

gene_expression_selected = pd.read_csv(project_dir / "data" / "processed" / "gene_expression_2000.csv",index_col="SAMPLE_ID")

clusters = pd.read_csv(project_dir / "data" / "processed" / "patient_clusters.csv",index_col="SAMPLE_ID")

print("Gene expresion data", gene_expression_selected.shape)
print("Cluster data", clusters.shape)
print("Match IDs expression -clusters", gene_expression_selected.index.isin(clusters.index).sum())


## Avg gene expressions
##====================================

expression_clusters = gene_expression_selected.join(clusters)

mean_exp = expression_clusters.groupby("Cluster").mean()

print("\nMean Gene Expression", mean_exp.shape)
print(mean_exp.iloc[:,:5])


mean_difference = mean_exp.loc[0] - mean_exp.loc[1]
mean_difference = mean_difference.sort_values(key=abs, ascending= False)
print(mean_difference.head(10))


## Top genes in clusters

print("\nTop 10 in Cluster 0", mean_difference.sort_values(ascending=False).head(10))

print("Top 10 in Cluster 1", mean_difference.sort_values(ascending=True).head(10))


## Save

gene_results = pd.DataFrame({"Gene": mean_difference.index,"Cluster_0_Mean": mean_exp.loc[0, mean_difference.index].values,"Cluster_1_Mean": mean_exp.loc[1, mean_difference.index].values,"Mean_Difference": mean_difference.values})

gene_results.to_csv(project_dir / "output" / "gene_expression_differences.csv",index=False)

print(gene_results.head())