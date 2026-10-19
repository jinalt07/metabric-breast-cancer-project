## 1. Overview

Unsupervised K-means clustering (k = 2) was performed using the first 20 principal components derived from the 2,000 most variable genes across 1,980 METABRIC breast cancer samples.

The analysis identified two patient groups: Cluster 0 (n = 1,414) and Cluster 1 (n = 566). These groups differed in their gene-expression patterns and clinical characteristics, including estrogen receptor (ER) status, HER2 status, tumor grade, molecular subtype, and age at diagnosis.

The biological interpretation focuses on identifying the molecular processes represented by the genes that differ most strongly between clusters and evaluating whether these patterns agree with established breast cancer biology.

## 2. Cluster 0: Estrogen Receptor Signaling and Luminal Differentiation

Cluster 0 showed higher average expression of several genes associated with estrogen receptor signaling and luminal breast cancer characteristics.

| Gene | Expression Difference (C0 − C1) | Biological Relevance |
|---|---:|---|
| ESR1 | +3.85 | Encodes estrogen receptor alpha, which regulates estrogen-responsive gene expression. |
| AGR3 | +3.79 | Associated with ER-positive and luminal breast cancer expression patterns. |
| TFF3 | +3.56 | Associated with hormone-responsive and luminal breast cancer characteristics. |
| TFF1 | +3.44 | A well-established estrogen-responsive gene. |
| ANKRD30A | +3.07 | Breast-associated gene expressed in subsets of breast tumors. |
| CA12 | +2.94 | Encodes carbonic anhydrase XII, associated with ER-positive breast cancer. |
| SRARP | +2.86 | Associated with steroid hormone receptor-related signaling in breast cancer. |
| SCUBE2 | +2.79 | Associated with luminal and hormone receptor-positive breast cancer. |
| FOXA1 | +2.77 | Pioneer transcription factor that facilitates estrogen receptor binding to DNA. |
| GATA3 | +2.70 | Transcription factor involved in mammary luminal cell differentiation. |

### Biological Interpretation

Three genes are particularly important for understanding this cluster:

- **ESR1:** Produces estrogen receptor alpha, which allows cells to respond to estrogen and regulate downstream gene expression.
- **FOXA1:** Helps open regulatory regions of DNA, allowing estrogen receptors to access their target genes.
- **GATA3:** Supports the differentiation and maintenance of luminal mammary epithelial cells.

Together, ESR1, FOXA1, and GATA3 participate in a regulatory network associated with estrogen-responsive transcription and luminal cell identity.

The higher expression of TFF1, TFF3, AGR3, and other luminal-associated genes provides additional support for this interpretation.

### Connection with Clinical Findings

- 97.81% of patients in Cluster 0 were ER-positive.
- 80.90% belonged to the Luminal A or Luminal B molecular subtypes.
- 37.17% of patients with available tumor-grade information had Grade 3 tumors.
- Mean age at diagnosis was 63.22 years.

These clinical findings agree with the molecular pattern, suggesting that Cluster 0 predominantly represents tumors with luminal differentiation and estrogen-receptor-associated signaling.

## 3. Cluster 1: Basal-Like, Inflammatory, and Metabolic Characteristics

Cluster 1 showed higher average expression of genes associated with inflammatory processes, basal-like tumor characteristics, cellular differentiation, and metabolism.

| Gene | Expression Difference (C0 − C1) | Potential Biological Relevance |
|---|---:|---|
| S100A8 | −2.81 | Inflammatory signaling and tumor microenvironment interactions. |
| S100A9 | −2.73 | Inflammation and immune-related processes; often functions alongside S100A8. |
| RARRES1 | −2.41 | Retinoid-related regulation and cellular differentiation. |
| PROM1 | −1.99 | Encodes CD133, a marker associated with certain stem-like cell populations. |
| PSAT1 | −1.97 | Serine biosynthesis and cellular metabolism. |
| FDCSP | −1.97 | Secreted protein associated with immune-related tissues and processes. |
| GABRP | −1.91 | Reported in basal-like and triple-negative breast cancer contexts. |
| KRT81 | −1.89 | Keratin-associated epithelial characteristics. |
| MMP7 | −1.86 | Extracellular matrix remodeling and tissue interactions. |
| BCL11A | −1.84 | Transcriptional regulation and basal-like breast cancer-associated biology. |

*Negative differences indicate higher mean expression in Cluster 1.*

### Biological Interpretation

The genes elevated in Cluster 1 suggest several potential biological themes:

**Inflammatory and immune-related processes:** S100A8 and S100A9 are involved in inflammatory signaling. Their higher expression may reflect inflammatory activity within tumors or contributions from immune cells in the surrounding tumor microenvironment.

**Basal-like characteristics:** GABRP and BCL11A have been associated with basal-like or triple-negative breast cancer biology. Their expression is consistent with the higher prevalence of basal tumors in this cluster.

**Cellular metabolism:** PSAT1 participates in serine biosynthesis, a metabolic pathway that supports cellular functions including the production of molecules needed for growth. Its higher expression suggests a possible metabolic distinction between clusters.

**Differentiation and tissue interactions:** PROM1, RARRES1, KRT81, and MMP7 are connected to aspects of cell identity, differentiation, or tissue remodeling. Their specific roles in this cluster require cautious interpretation.

These observations suggest biological themes rather than confirmed pathway activation. No formal pathway-enrichment analysis has yet been performed.

### Connection with Clinical Findings

- 78.27% of patients in Cluster 1 were ER-negative.
- 68.73% belonged to the Basal or Claudin-low molecular subtypes.
- 82.90% of patients with available tumor-grade information had Grade 3 tumors.
- 24.73% were HER2-positive, compared with 7.57% in Cluster 0.
- Mean age at diagnosis was 55.76 years.

These findings are consistent with a cluster enriched for tumors with basal-like and less differentiated characteristics, although the cluster contains multiple established molecular subtypes.

## 4. Comparison of Biological Processes

| Biological Feature | Cluster 0 | Cluster 1 |
|---|---|---|
| Dominant expression pattern | Luminal and estrogen-associated | Basal-like and inflammatory-associated |
| Representative genes | ESR1, FOXA1, GATA3, TFF1 | S100A8, S100A9, GABRP, BCL11A |
| Estrogen receptor signaling | Strongly represented | Less prominent |
| Luminal differentiation | Strongly represented | Less prominent |
| Inflammatory signals | Less prominent among top distinguishing genes | More prominent among top distinguishing genes |
| Metabolic characteristics | Not specifically evaluated | PSAT1 suggests possible serine metabolism involvement |
| Clinical associations | Predominantly ER-positive, Luminal A/B | Enriched for ER-negative, Basal/Claudin-low, Grade 3 tumors |

These are relative interpretations of the observed gene-expression patterns, not direct measurements of biological pathway activity.

## 5. Overall Interpretation and Relevance to Patient Heterogeneity

The findings suggest that unsupervised clustering of breast cancer gene-expression profiles can recover biologically meaningful patterns that correspond to established differences among breast tumors.

Cluster 0 predominantly reflects estrogen receptor signaling and luminal differentiation, supported by higher expression of ESR1, FOXA1, GATA3, and other estrogen-associated genes. Cluster 1 shows a contrasting pattern involving basal-like characteristics, inflammatory signals, and potential metabolic differences.

These molecular distinctions align with differences in ER status, HER2 status, tumor grade, molecular subtype, and age at diagnosis. In particular, Cluster 1 contains a substantially higher proportion of Grade 3 and ER-negative tumors, whereas Cluster 0 is dominated by ER-positive and Luminal A/B tumors.

The results therefore suggest that gene-expression variation captures important aspects of breast cancer heterogeneity beyond differences in individual genes. However, the two clusters are not biologically uniform, and their boundaries should not be treated as definitive disease categories.

## 6. Limitations of Biological Interpretation

1. **Established subtype overlap:** The clusters largely reflect previously recognized breast cancer characteristics rather than demonstrating the discovery of new molecular subtypes.
2. **Limited cluster separation:** The silhouette score for k = 2 was approximately 0.219, indicating modest separation between patient groups.
3. **Non-independent gene differences:** The same expression data were used for clustering and gene comparison. Therefore, the observed gene differences describe the clusters but do not independently validate them.
4. **Expression-derived molecular subtypes:** Agreement with established molecular subtype labels is informative but not independent confirmation because those labels are also based on gene-expression patterns.
5. **Bulk tumor expression:** Inflammatory gene signals may originate from tumor cells, surrounding immune cells, or other components of the tumor microenvironment.
6. **No functional validation:** The analysis does not directly measure pathway activity, protein abundance, or the causal roles of individual genes.
7. **Observational associations:** Differences in age, grade, and receptor status do not establish causal relationships.

## 7. Conclusion

The analysis identified two reproducible gene-expression-based patient groups with contrasting molecular and clinical characteristics. Cluster 0 was predominantly associated with estrogen receptor signaling and luminal differentiation, whereas Cluster 1 was enriched for basal-like characteristics, inflammatory-associated genes, and higher-grade tumors.

Overall, the findings demonstrate how unsupervised learning can help characterize breast cancer patient heterogeneity and recover established biological patterns from high-dimensional gene-expression data.

The results should be viewed as an exploratory characterization of breast cancer heterogeneity rather than evidence of novel molecular subtypes.

## 8. References

Relevant peer-reviewed literature supporting the biological functions and breast cancer associations of the identified genes will be added after verification.

--------------------------------------------------------------------


## Summary of Clinical and Molecular Findings

**Table 1. Clinical and molecular characteristics of the two METABRIC patient clusters.**

| Characteristic | Cluster 0 | Cluster 1 |
|---|---|---|
| Number of samples | 1,414 | 566 |
| ER-positive | 97.81% | 21.73% |
| HER2-positive | 7.57% | 24.73% |
| Grade 1 | 11.94% | 1.47% |
| Grade 2 | 50.89% | 15.62% |
| Grade 3 | 37.17% | 82.90% |
| Luminal A/B | 80.90% | 5.48% |
| Basal/Claudin-low | 2.69% | 68.73% |
| Mean age at diagnosis | 63.22 years | 55.76 years |
| Representative higher-expression genes | ESR1, FOXA1, GATA3 | S100A8, S100A9, GABRP |

**Notes:**
- Tumor-grade percentages exclude samples with missing grade information.
- Molecular subtype percentages are calculated within each cluster.
- Gene-expression differences are descriptive and do not establish causation.
- All five clinical comparisons remained statistically significant after Benjamini–Hochberg correction. The molecular subtype chi-square test has a limitation involving small expected counts.
