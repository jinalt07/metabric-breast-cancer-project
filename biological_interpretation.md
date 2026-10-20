### Biological Interpretation of METABRIC Breast Cancer Patient Clusters

### 1. Overview

Unsupervised K-means clustering (k = 2) was performed using the first 20 principal components derived from the 2,000 most variable genes across 1,980 METABRIC breast cancer samples.

The analysis identified two patient groups: Cluster 0 (n = 1,414) and Cluster 1 (n = 566). These groups differed in their gene-expression patterns and clinical characteristics, including estrogen receptor (ER) status, HER2 status, tumor grade, molecular subtype, and age at diagnosis.

The biological interpretation focuses on identifying the molecular processes represented by the genes that differ most strongly between clusters and evaluating whether these patterns agree with established breast cancer biology.

### 2. Cluster 0: Estrogen Receptor Signaling and Luminal Differentiation

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

**Biological Interpretation**

ESR1, FOXA1, and GATA3 provide a useful framework for interpreting this cluster. ESR1 encodes estrogen receptor alpha; FOXA1 facilitates access to regulatory DNA regions; and GATA3 contributes to luminal epithelial identity. Together, these genes are associated with estrogen-responsive transcriptional programs in breast cancer.

The higher expression of TFF1, TFF3, AGR3, and other luminal-associated genes is consistent with this pattern. These associations reflect prior biological knowledge, not mechanisms directly tested in the present analysis (Perou et al., 2000; Sørlie et al., 2001; Parker et al., 2009).

**Connection with Clinical Findings**

Cluster 0 was 97.81% ER-positive, and 80.90% of its samples were classified as Luminal A or Luminal B. Among samples with available tumor-grade information, 37.17% were Grade 3. Mean age at diagnosis was 63.22 years.

Together, these observations support describing Cluster 0 as predominantly luminal and estrogen-associated, rather than as a single uniform molecular subtype.

### 3. Cluster 1: Basal-Like, Inflammatory, and Metabolic Characteristics

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

**Biological Interpretation**

**Inflammatory-associated genes**

S100A8 and S100A9 are associated with inflammatory and immune-related processes. Their higher expression may reflect signals from tumor cells, infiltrating immune cells, or other components of the tumor microenvironment. Bulk tumor expression data cannot distinguish these sources without additional analysis.

**Basal-like characteristics**

GABRP and BCL11A have been reported in basal-like or triple-negative breast cancer contexts. Their higher expression is consistent with the greater representation of basal-like tumors in Cluster 1, but neither gene alone establishes a subtype classification.

**Metabolism-related expression**

PSAT1 encodes an enzyme involved in serine biosynthesis. Its higher expression suggests a difference in this metabolism-related transcript, but does not establish increased serine-pathway activity or a broader metabolic shift.

**Cell identity and tissue interactions**

PROM1, RARRES1, KRT81, and MMP7 have reported associations with cellular identity, differentiation, or tissue remodeling. Their roles in the observed cluster differences remain uncertain.

**Connection with Clinical Findings**

Cluster 1 was 78.27% ER-negative, and 68.73% of its samples were classified as basal-like or claudin-low.

Among samples with available tumor-grade information, 82.90% were Grade 3. HER2-positive tumors represented 24.73% of Cluster 1, compared with 7.57% of Cluster 0. Mean age at diagnosis was 55.76 years.

These findings support describing Cluster 1 as enriched for ER-negative, higher-grade, and basal-like/claudin-low tumors, while recognizing that it includes several molecular subtypes (Perou et al., 2000; Sørlie et al., 2001; Curtis et al., 2012).

### 4. Comparison of Biological Processes

| Feature | Cluster 0 | Cluster 1 |
|---|---|---|
| Predominant expression association | Estrogen-associated and luminal | Basal-like and inflammatory-associated |
| Representative higher-expression genes | ESR1, FOXA1, GATA3, TFF1 | S100A8, S100A9, GABRP, BCL11A |
| Estrogen-associated transcripts | Higher expression of several associated genes | Less prominent among the top distinguishing genes |
| Luminal-associated transcripts | Higher expression of several associated genes | Less prominent among the top distinguishing genes |
| Inflammatory-associated transcripts | Less prominent among the top distinguishing genes | S100A8 and S100A9 higher |
| Metabolism-related transcript | No pathway-level conclusion | PSAT1 higher; pathway activity not assessed |
| Main clinical pattern | Predominantly ER-positive and Luminal A/B | Enriched for ER-negative, basal-like/claudin-low, and Grade 3 tumors |

### 5. Overall Interpretation and Relevance to Patient Heterogeneity

The identified clusters demonstrate that variation in breast cancer gene-expression profiles corresponds to differences in established molecular and clinical characteristics.

Although clinical labels were not used to construct the clusters, the resulting groups differed substantially in receptor status, tumor grade, molecular subtype distribution, and age at diagnosis.

The results suggest that unsupervised clustering can recover broad patterns of breast cancer heterogeneity.

However, the groups are not biologically uniform, and their correspondence with established subtypes should not be interpreted as the discovery of new disease categories.

In addition, expression-derived molecular subtype labels do not constitute fully independent validation of expression-based clusters.

### 6. Limitations of Biological Interpretation

1. **Established subtype overlap:** The clusters largely reflect previously recognized breast cancer characteristics rather than demonstrating the discovery of new molecular subtypes.

2. **Limited cluster separation:** The silhouette score for k = 2 was approximately 0.219, indicating modest separation between patient groups.

3. **Non-independent gene differences:** The same expression data were used for clustering and gene comparison. Therefore, the observed gene differences describe the clusters but do not independently validate them.

4. **Expression-derived molecular subtypes:** Agreement with established molecular subtype labels is informative but not independent confirmation because those labels are also based on gene-expression patterns.

5. **Bulk tumor expression:** Inflammatory gene signals may originate from tumor cells, surrounding immune cells, or other components of the tumor microenvironment.

6. **No functional validation:** The analysis does not directly measure pathway activity, protein abundance, or the causal roles of individual genes.

7. **Observational associations:** Differences in age, grade, and receptor status do not establish causal relationships.

### 7. Conclusion

This exploratory analysis identified two stable gene-expression-based patient groups with contrasting clinical and molecular characteristics.

Their differences largely align with established luminal and basal-like breast cancer patterns rather than indicating novel molecular subtypes.

Formal differential-expression testing, pathway enrichment, independent-cohort evaluation, and clinical outcome analyses would be needed to characterize the biological and clinical relevance of these groups more comprehensively.

### 8. References

Curtis, C., et al. (2012). *The genomic and transcriptomic architecture of 2,000 breast tumours reveals novel subgroups.* Nature, 486(7403), 346–352. https://doi.org/10.1038/nature10983

Parker, J. S., et al. (2009). *Supervised risk predictor of breast cancer based on intrinsic subtypes.* Journal of Clinical Oncology, 27(8), 1160–1167. https://doi.org/10.1200/JCO.2008.18.1370

Perou, C. M., et al. (2000). *Molecular portraits of human breast tumours.* Nature, 406(6797), 747–752. https://doi.org/10.1038/35021093

Sørlie, T., et al. (2001). *Gene expression patterns of breast carcinomas distinguish tumor subclasses with clinical implications.* Proceedings of the National Academy of Sciences, 98(19), 10869–10874. https://doi.org/10.1073/pnas.191367098

### Summary of Clinical and Molecular Findings

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
