from pathlib import Path
import pandas as pd

project_dir = Path(__file__).resolve().parent.parent

clinical = pd.read_csv(project_dir / "data" / "processed" / "clinical_merged.csv")

clusters = pd.read_csv(project_dir / "data" / "processed" / "patient_clusters.csv")

clinical_clusters = clinical.merge(clusters, on= "SAMPLE_ID", how="inner")

print(clinical_clusters.shape)
print(clinical_clusters[["SAMPLE_ID", "Cluster"]].head())


## Compare ER
##==================================

er_comparison = pd.crosstab(clinical_clusters["Cluster"], clinical_clusters["ER_STATUS"])
print(er_comparison)

er_percentage = pd.crosstab(clinical_clusters["Cluster"], clinical_clusters["ER_STATUS"], normalize="index")*100
print(er_percentage.round(2))

## Compare HER2
##=================================

her2_comparisom = pd.crosstab(clinical_clusters["Cluster"], clinical_clusters["HER2_STATUS"])
print(her2_comparisom)

her2_percentage = pd.crosstab(clinical_clusters["Cluster"], clinical_clusters["HER2_STATUS"], normalize="index")*100
print(her2_percentage.round(2))


print([col for col in clinical_clusters.columns if "GRADE" in col.upper()])

## Compare Tumor Grade
##==================================

grade_comparison = pd.crosstab(clinical_clusters["Cluster"], clinical_clusters["GRADE"])
print(grade_comparison)

grade_comparison_percentage = pd.crosstab(clinical_clusters["Cluster"], clinical_clusters["GRADE"], normalize="index")*100
print(grade_comparison_percentage.round(2))

## Compare Molecular Subtype
##==================================

subtype_comparison = pd.crosstab(clinical_clusters["Cluster"], clinical_clusters["CLAUDIN_SUBTYPE"])
print(subtype_comparison)

subtype_percentages = pd.crosstab(clinical_clusters["Cluster"],clinical_clusters["CLAUDIN_SUBTYPE"],normalize="index") * 100
print(subtype_percentages.round(2))

## Age check
##===================================

age_comparison = clinical_clusters.groupby("Cluster")["AGE_AT_DIAGNOSIS"].agg(["count", "mean", "median", "std"])
print(age_comparison.round(2))


##============================================
## Statistical Testing
##============================================

## ER Status - Chi Square
##===================================

from scipy.stats import chi2_contingency

chi2, p_value, dof, expected = chi2_contingency(er_comparison)

print("\nChi-square statistic", round(chi2, 2))
print("p-value", p_value)

## HER2 Status - Chi Sqaure
##==================================

chi2_her2, p_value_her2, dof_her2, expected_her2 = chi2_contingency(her2_comparisom)

print("\nHER2 Chi-square statistic", round(chi2_her2, 2))
print("HER2 p-value", p_value_her2)

## Tumor Grade - Cho Square
##=====================================

chi2_grade, p_value_grade, dof_grade, expected_grade = chi2_contingency(grade_comparison)

print("\nGrade chi-square statistic:", round(chi2_grade, 2))
print("Grade p-value:", p_value_grade)

## Molecular Subtype - Chi Square
##==================================

chi2_subtype, p_value_subtype, dof_subtype, expected_subtype = chi2_contingency(subtype_comparison)

print("\nSubtype Chi-square statistic", round(chi2_subtype,2))
print("Subtype p-value", p_value_subtype)

## Age - t-test
##====================================

from scipy.stats import ttest_ind

age_cluster_0 = clinical_clusters.loc[clinical_clusters["Cluster"] == 0, "AGE_AT_DIAGNOSIS"].dropna()

age_cluster_1 = clinical_clusters.loc[clinical_clusters["Cluster"] == 1, "AGE_AT_DIAGNOSIS"].dropna()

t_stat, p_value_age = ttest_ind(age_cluster_0, age_cluster_1, equal_var=False)

print("\nAge t-statistic", round(t_stat, 2))
print("Age p-value", p_value_age)

###############################

from statsmodels.stats.multitest import multipletests
import pandas as pd

p_values = [ 1.863e-280,3.384e-25, 9.736e-72, 1.088e-274, 8.931e-30]

adjusted_p =multipletests(p_values, method= "fdr_bh")[1]

results = pd.DataFrame({ "Variable": ["ER Status", "HER2 Status", "Tumor Grade", "Molecular Subtype", "Age at Diagnosis"],
                        "Original p-value": p_values,
                        "Adjusted p-value": adjusted_p})

print(results)

