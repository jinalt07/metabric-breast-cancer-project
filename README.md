# Identifying Patient Heterogeneity in Breast Cancer Using METABRIC Data

## Project Overview

This project explores patient heterogeneity in breast cancer using unsupervised machine learning applied to gene-expression data from the METABRIC study.

The analysis investigates whether patients can be grouped according to similarities in their gene-expression profiles and how these groups relate to available clinical characteristics.

The project was developed as an independent computational research exercise, with an emphasis on implementing an end-to-end analytical workflow, interpreting results, and evaluating methodological limitations.

## Dataset

**Source:** METABRIC (Molecular Taxonomy of Breast Cancer International Consortium), accessed through [cBioPortal](https://www.cbioportal.org/).

The analysis uses processed gene-expression measurements alongside patient-level and sample-level clinical information.

- **Initial clinical records:** 2,509
- **Matched samples used for analysis:** 1,980
- **Genes selected for analysis:** 2,000 highly variable genes

The original dataset is not included in this repository. It can be obtained from cBioPortal.

## Analytical Workflow

The analysis was implemented in Python and organized into seven scripts:

| Script | Purpose |
|---|---|
| `01_data_exploration.py` | Load, inspect, preprocess, and match molecular and clinical data |
| `02_pca.py` | Perform PCA and examine explained variance |
| `03_clusters.py` | Apply K-means clustering and evaluate cluster numbers |
| `04_clinical_analysis.py` | Compare clinical characteristics between clusters |
| `05_gene_analysis.py` | Identify genes with prominent mean-expression differences |
| `06_cluster_validation.py` | Evaluate cluster stability under alternative settings |
| `07_charts.py` | Generate visualizations of the analysis |

The workflow combines dimensionality reduction, unsupervised clustering, statistical comparisons, and stability assessment.

## Key Results

The analysis identified two patient clusters comprising 1,414 and 566 samples.

The clusters differed in receptor status, tumor grade, molecular subtype distribution, age at diagnosis, and gene-expression patterns. Cluster assignments were highly stable under the tested settings, although separation between the groups was modest.

The findings broadly corresponded to established breast cancer molecular characteristics rather than suggesting a new subtype classification.

For detailed statistics, visualizations, and interpretation, refer to the research report.

## Repository Structure

```text
metabric-breast-cancer-project/
│
├── data/
│   └── processed/             # Local datasets (not tracked by Git)
│
├── src/                       # Python analysis scripts
│
├── output/
│   ├── figures/               # Generated visualizations
│   └── gene_expression_differences.csv
│
├── notebooks/                 # Reserved for exploratory notebooks
│
├── biological_interpretation.md
├── requirements.txt
└── README.md
```

## Project Documentation

**Research Report**

Provides the complete methodology, statistical results, visualizations, discussion, and limitations of the analysis.

**[Biological Interpretation](biological_interpretation.md)**

Examines the biological associations of genes distinguishing the clusters and explains how these patterns relate to established breast cancer characteristics.

**[Generated Figures](output/figures/)**

Contains PCA visualizations and comparisons of clinical and gene-expression characteristics.

**[Gene-Expression Results](output/gene_expression_differences.csv)**

Contains the calculated mean-expression differences between clusters.

## Tools and Methods

- **Language:** Python
- **Data processing:** pandas, NumPy
- **Machine learning:** PCA, K-means clustering, silhouette analysis
- **Statistical analysis:** Chi-square tests, Welch's t-test, Benjamini–Hochberg correction
- **Validation:** Adjusted Rand Index (ARI)
- **Visualization:** Matplotlib and related Python plotting tools

## Reproducibility

To work with the project locally:

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies using `pip install -r requirements.txt`.
4. Download the METABRIC gene-expression and clinical datasets from cBioPortal.
5. Place the datasets in the local `data/` directory.
6. Execute the analysis scripts in numerical order.

The analysis uses fixed random seeds where applicable to support reproducibility. Original and reproduced clustering solutions showed high agreement, with minor assignment differences documented in the research report.

## Scope and Limitations

This is an exploratory computational analysis using one publicly available breast cancer cohort. The identified clusters should not be interpreted as newly established molecular subtypes or clinically validated patient classifications.

The project does not evaluate treatment response, survival outcomes, or clinical utility.

## Data Attribution

The METABRIC dataset was originally described by Curtis et al. (2012) and accessed through cBioPortal (Gao et al., 2013).

- Curtis et al. (2012). *The genomic and transcriptomic architecture of 2,000 breast tumours reveals novel subgroups.* Nature. https://doi.org/10.1038/nature10983
- Gao et al. (2013). *Integrative analysis of complex cancer genomics and clinical profiles using the cBioPortal.* Science Signaling. https://doi.org/10.1126/scisignal.2004088