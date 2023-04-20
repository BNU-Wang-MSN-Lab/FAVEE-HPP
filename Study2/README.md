# Preprocessing

- CheckDataQuality&TurnMatrixIntoAverageRDM.ipynb  
Ensure that both classification tasks have high data quality, and after removing the outlier, average the results for group-level analysis.   

- TurnMeadowIntoMatrix.ipynb  
Convert Meadows data into CSV format.  

# ModelsInTasks

Categorical and diemsional models derived from the three task in group level.

|Type| Models      | file        | Methods        | Num.participants  |
|------| ----------- | ----------- |----------- | ----------- |
|Categorical| M1 M2      | M1M2_Group_cat_clustering_159r.ipynb | UMAP+KMeans|59|
|Dimensional| M4 M5      | M4M5_Group_cat_dimension_159r.ipynb | MDS+Regression|59|
|Dimensional| M3 |M3M6M7_Group_dim_dimension_clustering_159r.ipynb| PCA| 14|
|Categorical| M6 |M3M6M7_Group_dim_dimension_clustering_159r.ipynb| UMAP+KMeans| 14|
|Categorical| M7 |M3M6M7_Group_dim_dimension_clustering_159r.ipynb| PCA+KMeans| 14|

# LoocvModelCompare

At the individual level, repeat the group process for obtaining model shown in __"Individual_analysis"__.  
- Individual_cat_dimension_159r.ipynb  
    - Tasks: multi-arrangement and free sorting tasks
    - Models: M4 M5  

- Individual_dim_dimension_159r.ipynb  
    - Tasks: Dimensional Survey
    - Models: M6 

- Individual_catdim_category_159r.ipynb
    - Tasks: multi-arrangement, free sorting tasks and Dimensional Survey
    - Models: M1 M2 M3 M7 

To access the intra-individual generalizability of each categorical and dimensional model, we did a Leave-One-Out-Cross-Validation test. For each statistical model, we generated a model for every single participant and a model for the left participants. We then calculated the Spearman correlation between these two models (i.e., inter-subject correlation (ISC)). A higher value indicates higher similarity between the single participant and the left-over participants (i.e., higher generalizability). We compared the mean ISC value of each model. The results indicated that the categorical model for the dimensional survey (Model 3), the dimensional model for the dimensional survey (Model 6), and the categorical model for FAVEE space (Model 7) had higher generalizability.  

- The detailed processes of LOOCV are shown in files starting with "LOOCV".  
- The model and task comparison are shown in corresponding files.

# TextAnalysis

To verify the categorical models. We conducted a text analysis of labels assigned by participants to the classification they freely sorted 159 relationships into. After pooling the results of all 60 participants, we obtained a total of 444 labels, including duplicates. Labels represent one type of relationship; conversely, whether a relationship falls under a given label can be regarded as a characteristic of that label. Each label contains 159 features containing values 0 or 1, and one indicates that this relationship is included in the label, while zero indicates that it is not. By combining all 444 labels, we obtained a matrix with 444 rows and 159 columns. For instance, the ‘family’ label included ‘Wife - Husband’ rather than ‘Doctor - Patient’; therefore, the former column contains one while the latter contains zero. A Hierarchical Agglomerative Clustering (HAC) was performed on this organized matrix. Firstly, we were constantly getting a cluster containing mixed labels, such as 'distant', 'neutral', 'religious', 'sport', 'mentor', 'mentee', 'caretaker', 'familial', etc. __(HAC_results_first.csv)__ We then excluded these mixed labels, resulting in a matrix with 292 rows left, which resulted in 3 or 6 meaningful clusters based on HAC analysis __(HAC_results_final.csv)__. The cluster results are identical to those found in the main text in Study 2.   

- The codes of clustering labels: Label analysis in explicit task.ipynb  
- Visualization of clustering results: Plot results.ipynb

# FAVEE-HPP correlation

Correlation analysis suggested that the FAVEE and HPP models were relatively independent of each other (e.g., shared variance < 18%).

