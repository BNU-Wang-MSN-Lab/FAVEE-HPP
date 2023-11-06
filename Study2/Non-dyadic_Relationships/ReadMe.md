**Non-Dyadic social relationships**

# Rel_Group

We performed the principal component analysis(PCA) on the datasets of 40 group relationships collected in USA and CHN. 

## file

- input_data - here are two waves of raw data collected in China(Naodao) and one wave of raw data collected in USA(Cloud Research),<br> here are also "group_relationships_fix_label.csv" and "qualtrics_question_key.csv" to form a matrix with rows that are group relationships and columns that are evaluative features. 

- output_data - here are cleaning results and pca results, dict_results could be helpful to display the variances of each evaluative features. 

- output_graph - figures of usa pca loadings shown in main text. 

- raw_data - raw data downloaded from Naodao and Cloud Research. 

## code

- CHN_DataCleanPCA_All_group.ipynb - performed the data cleaning and PCA in data from China(1st wave)

- CHN_DataCleanPCA_group.ipynb - performed the data cleaning and PCA in data from China(2ed wave)

- USA_DataCleanPCA_group.ipynb - performed the data cleaning and PCA in data from USA



# Rel_Triadic

We performed the principal component analysis(PCA) on the datasets of 34 triadic relationships collected in USA and CHN. 

## file

- input_data - here are two waves of raw data collected in China(Naodao) and one wave of raw data collected in USA(Cloud Research),<br> here are also "triadic_relationships_fix_label.csv" and "qualtrics_question_key.csv" to form a matrix with rows that are triadic relationships and columns that are evaluative features. 

- output_data - here are cleaning results and pca results, dict_results could be helpful to display the variances of each evaluative features. 

- output_graph - figures of the scree and the pca loadings. 

- raw_data - raw data downloaded from Naodao and Cloud Research. 

## code

- CHN_DataCleanPCA_All_triadic.ipynb - performed the data cleaning and PCA in data from China(1st wave)

- CHN_DataCleanPCA_triadic.ipynb - performed the data cleaning and PCA in data from China(2ed wave)

- USA_DataCleanPCA_triadic.ipynb - performed the data cleaning and PCA in data from USA

  

# HSR_concat

We concatenated the Group and Triadic relationships as the relationships we called "non-dyadic relationships". The results were saved in the folder named "Concat_Group_and_Triadic_All". Subsequently, we conducted PCA and generated scattered plots to gain deeper insights into these non-dyadic relationships. 

## file

- input_data - data have been concatenated

- output_data - loadings and scores of the data of the none-dyadic relationships

- output_graph - figures of the loadings and the scatter plots

## code

- Concat_Group_and_Triadic_All/PCA_GT.ipynb - performed PCA in data from the USA

- Concat_Group_and_Triadic_All/usa_GT_scattered_plot.ipynb - scattered plots



# Rel_Dyadic

We performed the principal component analysis(PCA) on the datasets of dyadic relationships collected in USA and CHN, to measure the similarity between dyadic relationships and non-dyadic relationships. 

Dyadic data were obtained from US-China comparison in Study2.

## file

- output_data - here are cleaning results and pca results

## code

- CHN_DataCleanPCA.ipynb - performed the data cleaning and PCA in data from China

- USA_DataCleanPCA.ipynb - performed the data cleaning and PCA in data from USA



# Loading_rsa

We conducted rsa to demonstrate the congruence between human relationships of different structures. 

## file

- output_data - chn & usa correlations
- output_graph - figures of the rsa results

## code

- RSA_33d_analysis.ipynb - performed the RSA among the dyadic relationships and the non-dyadic relationships and other relationships