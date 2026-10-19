from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent

data= project_dir / "data"

gene_expression_file = data / "data_mrna_illumina_microarray_DATA.txt"
clinical_sample_file = data/ "data_clinical_sample_DATA.txt"
clinical_patient_file = data/ "data_clinical_patient_DATA.txt"

print("Gene expression:", gene_expression_file.is_file())
print("Clinical sample:", clinical_sample_file.is_file())
print("Clinical patient:", clinical_patient_file.is_file())

##=========================================
## Data Loading
##=========================================

## 1. Clinical Patient Data
##=========================================

import pandas as pd

clinical_patient= pd.read_csv(clinical_patient_file, sep =r"\t", skiprows=4)
print(clinical_patient.shape)
print(clinical_patient.head())
print(clinical_patient.columns.tolist())
print(clinical_patient.isnull().sum())

## 2. Clinical Sample Data
##=======================================

clinical_sample = pd.read_csv(clinical_sample_file, sep="\t", skiprows=4)
print(clinical_sample.shape)
print(clinical_sample.head())

print("Unique patients:", clinical_sample["PATIENT_ID"].nunique())
print("Unique samples:", clinical_sample["SAMPLE_ID"].nunique())
print("\n Checking both IDS")
print((clinical_sample["PATIENT_ID"] == clinical_sample["SAMPLE_ID"]).all())

## 3. Gene Expression Data
##======================================

gene_expression = pd.read_csv(gene_expression_file, sep="\t", nrows=5)
print(gene_expression.shape)
#print(gene_expression.columns.to_list())

## Cross check sample IDs

gene_sample_ids = gene_expression.columns[2:]
match_samples = gene_sample_ids.isin(clinical_sample["SAMPLE_ID"])

print("\nMatching samples:", match_samples.sum())
print("Non-matching samples:", (~match_samples).sum())

total_genes = pd.read_csv(gene_expression_file, sep= "\t", usecols=["Hugo_Symbol", "Entrez_Gene_Id"])
print("Total gene rows:", total_genes.shape[0])
print("Unique genes:", total_genes["Hugo_Symbol"].nunique())
print("Missing gene symbols:", total_genes["Hugo_Symbol"].isna().sum())

## Duplicate gene counts

gene_counts = total_genes["Hugo_Symbol"].value_counts()
duplicate_genes = gene_counts[gene_counts > 1]
print("Number of duplicated genes:", duplicate_genes.shape[0])
print("\nMost frequently repeated genes:")
print(duplicate_genes.to_string())

## Check expression values

trdv2 = pd.read_csv(gene_expression_file, sep= "\t", usecols=["Hugo_Symbol", "MB-0362", "MB-0346"])
print(trdv2[trdv2["Hugo_Symbol"] == "TRDV2"])

## Whole gene expression data- check missing values

gene_expression_full = pd.read_csv(gene_expression_file, sep="\t", dtype={"Hugo_Symbol": "string", "Entrez_Gene_Id": "string"})

print(gene_expression_full.shape)
print(gene_expression_full.isna().sum().sum())
missing_col = gene_expression_full.isna().sum()
print(missing_col[missing_col > 0])


missing_genes = gene_expression_full[gene_expression_full.iloc[:, 2:].isna().any(axis=1)]
print(missing_genes[["Hugo_Symbol"]].assign(Missing_Count=missing_genes.iloc[:, 2:].isna().sum(axis=1)).to_string(index=False))


## Match whole Data
##=============================================

match_patients = clinical_sample[clinical_sample["SAMPLE_ID"].isin(gene_expression_full.columns[2:])]
print("\nMatching / Similar samples:", len(match_patients))
print("\nMatch Patients:", match_patients["PATIENT_ID"].isin(clinical_patient["PATIENT_ID"]).sum())

##=============================================
## Merge Data Set
##=============================================

## Clinical Data

clinical_merged = match_patients.merge(clinical_patient, on= "PATIENT_ID", how= "left")

print("\nMerged Data")
print(clinical_merged.shape)
print(clinical_merged.head())
print(clinical_merged.columns.to_list())

clinical_merged.to_csv(project_dir/ "data" / "processed" / "clinical_merged.csv", index= False)

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
##==================================================
## Gene Expression Data Preparation
##==================================================

## Missing Values

expression_val = gene_expression_full.iloc[:,2:]
gene_expression_full.iloc[:,2:] = expression_val.T.fillna(expression_val.mean(axis=1)).T
print("Missing values after cleaning:", gene_expression_full.iloc[:,2:].isna().sum().sum())

## Duplicate Values

gene_expression_clean = gene_expression_full.groupby("Hugo_Symbol", as_index=False).mean(numeric_only=True)
print("\nClean gene data")
print(gene_expression_clean.shape)
print(gene_expression_clean["Hugo_Symbol"].duplicated().sum())

## Transpose Data for Principal Component Analysis (PCA)

gene_expression_tp = gene_expression_clean.set_index("Hugo_Symbol").T
gene_expression_tp.index.name = "SAMPLE_ID"

print("\nTranspose Data")
print(gene_expression_tp.shape)
print(gene_expression_tp.iloc[:5,:5])

gene_expression_tp.to_csv(project_dir / "data"/ "processed" / "gene_expression_trans.csv")

import numpy as np

print("\nNon-numeric columns:",len(gene_expression_tp.select_dtypes(exclude="number").columns))
print("Missing values:",gene_expression_tp.isna().sum().sum())
print("Infinite values:",np.isinf(gene_expression_tp.to_numpy(dtype=float)).sum())

## Checking Variance in Data

gene_varience = gene_expression_tp.var(axis=0)
print("\nTotal genes", len(gene_varience))
print("Top variable genes", gene_varience.sort_values(ascending = False).head(10))

## Selecting 2000 genes

top_genes = gene_varience.nlargest(2000).index
gene_expression_selected = gene_expression_tp[top_genes]
print("Top genes shape", gene_expression_selected.shape)

gene_expression_selected.to_csv(project_dir / "data" / "processed" / "gene_expression_2000.csv")