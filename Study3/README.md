# Clustering

Nineteen regions hierarchical clustering    
- clustering of 19 regions.ipynb  
We performed a hierarchical clustering to find which regions are similar to each other according to their social relationship representations. For each region, we generated a representational dissimilarity matrix (RDM) of the 159 relationships, by calculating their Euclidean distance on the 33 conceptual features. We calculated the Spearman correlation between regions’ relationship RDM and then used 1 minus the correlation value, resulting in a region-by-region RDM in which a higher value indicates higher dissimilarity between these two regions based on their social relationship representation. The RDM was first reduced to 2D space using UMAP and then hierarchical clustering was performed using the ‘hclust’ function in R.   

Categorical Model
- CategoricalModel_19regions&WorldAveragedModel.ipynb  
For the categorical model, we performed K-means clustering on the RDMs derived from each region as well as the averaged model.

# DataCleanPCA

- each_region  
Dimensional model via PCA in each region.  
- MeaningOf33D_AveragedWorldModelPCA.ipynb  
Each dimension's meaning in each region, calculated by spearman's correlation between the PCA scores in each region and the averaged scores across the 19 regions.

- Demographics  
    - Demographic_RDM.ipynb  
    Generate RDM for RSA regression  
    - Plot_demographics.ipynb  
    There is a visualization of demographic information across all studies, and detailed information can be found in "Demographics.xlsx".

# RSA_Regression

To access which cultural variables account for the variance of social relationship knowledge representation across countries/regions, we performed a multiple regression similarity analysis (RSA).  
- ../Cultural_RDM/Variables_rdm.ipynb  
We created a representational dissimilarity matrix (RDM) for each cultural variable in which each cell represents the dissimilarity of two countries/regions on this variable (e.g. how dissimilar China and Portugal are, according to their Modernization level). 
- Models_rdm.ipynb  
We also created an RDM to represent the dissimilarity of relationship representation across countries/regions.  
- RSA_Regression.ipynb / RSA_Regression_subvariables.ipynb  
We then performed a linear regression model in which cultural variable RDMs were predictors, relationship representation RDM was the response variable. For our purpose here, the regression RSA measures how the similarity structure of the response variable (i.e., relationship representation) may be predicted by the similarity of the predictive variables (e.g., Modernization, Languages, etc.).

# Cognition of relationships  
- Category perception.ipynb + LOOCV.ipynb   
Cultural variability on relationships and categories. Cross-region reliability is caculated by relationships or clusters in 33D space.  

- ReliabilityCrossRegions_159rels.ipynb  
There is no correlation between the difference in cultural variability and familiarity in relationships.

# Subset  
- Robustness/ Robustness Test.ipynb  
We quantified the robustness of our results across different numbers of social relationships as Lin (2021) did. We removed social relationships one by one and reperformed PCA to extract five dimensions as before (all pairs of social relationships were ranked from the most to the least similar rated in multi-arrangement task, and the social relationship with lower familiarity rating was removed from each pair). The correlations were calculated between the loadings of each dimension from the full set versus the subsets of relationships as the robustness of our results.  
- full&dimension_model.ipynb / category_model.ipynb + models_rdm.ipynb  
From the full set of each region, we derive the full feature, dimensional, and categorical models for each subset. Then we created RDMs to represent the dissimilarity of relationship representation across countries/regions.  
- regression_categorical.ipynb / regression_dimensional.ipynb / regression_full_feature.ipynb   
RSA regression results derived from the subset. We report the effect of modernization and religion on different models using the same RSA analysis procedural as mentioned above.  
- data    
The remaining subsets after removing one relationship at each step.

# Study3_CHNvsUSA  
There were two rounds of data collection for China. The relationships in the first round were directly translated from 159 relationships in the United States **(CHN_Trans_DataCleanPCA.ipynb)**, while the relationships in the second round were generated using NLP **(CHN_NLP_DataCleanPCA.ipynb)**. There was a high correlation between the translation results and the NLP results.

To compare CHN and USA, we combined the USA data from Study1 and Study3. **(USA_DataCleanPCA.ipynb)**.  

CHN VS USA:  
- Similarity_33&30d.ipynb  
The dimensional frameworks of the two countries are highly correlated.  
- Difference  
The different between the two countries in relationship knowledge.  
![Study3_CHNvsUSA.png](../graph/Study3_CHNvsUSA.png)

# Model_comparison
