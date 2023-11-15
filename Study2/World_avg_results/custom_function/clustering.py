#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'Clustering analysis for superheatmap'
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

# Set a random seem for replicability
random_seed = 2022

from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn_extra.cluster import KMedoids

from sklearn.metrics import silhouette_samples, silhouette_score
from scipy.cluster.hierarchy import ClusterWarning
from warnings import simplefilter

import matplotlib.pyplot as plt
import matplotlib.cm as cm
from adjustText import adjust_text
import itertools

import numpy as np

import umap.umap_ as umap
from sklearn.manifold import TSNE

"""
1.optimal clusters
1.1 optimalK_grouped(): prepare for optimal parameter
1.2.1 neigh_dist(): UMAP
1.2.2 perperlixty(): t-SNE

2.create models
2.1create_cluster_models(): create cluster models

3.print models
3.1 cluster_results(): print cluster models
3.2 scatter_top_num(): plot relationships distribution in 2-D space
3.3 silhouette_cluster: plot each cluster's silhouette score, and compare it with average score
"""

def optimalK_grouped(data_type, data, algorithm1, algorithm2, title, random_state=random_seed, maxClusters=8):
    """
    Calculates optimal K using silhouette score
    Params:
        data_type: df, dissim
        data: ndarry of shape (n_samples, n_features)
        algorithm1: kmeans, kmedoids, or hierarchical
        algorithm2: kmeans, kmedoids, or hierarchical
        title: the title for the resulting figure
        maxClusters: Maximum number of clusters to test for
    Returns: (silh, optimalK)
    """
    simplefilter("ignore", ClusterWarning)
    silh = np.zeros((len(range(1, maxClusters)),))
    resultsdf = pd.DataFrame({'algorithm':[], 'clusterCount':[], 'silhouette':[]})
    for algorithm in [algorithm1, algorithm2]:
        for index, k in enumerate(range(2, maxClusters)):

            # Fit cluster to original data and create dispersion
            ####################################################
            ###based on type of data, choose corresponding model
            ####################################################
            if algorithm == 'kmeans':
                model = KMeans(k, random_state=random_state)
                model.fit(data)
            if algorithm == 'kmedoids':
                model = KMedoids(n_clusters=k, metric="euclidean",
                                 random_state=random_state)
                model.fit(data)
            if algorithm == 'hierarchical':
                model = AgglomerativeClustering(n_clusters=k,linkage = 'average')
                model.fit(data)

            cluster_labels = model.fit_predict(data)
            silhouette_avg = silhouette_score(data, cluster_labels)
            
            ###############################################################################################
            ###When the Dissimilar Matrix is inputted in Clustering function,"precomputed" should be stated 
            ###############################################################################################
            if data_type == 'dissim':
                #Kmeans hasn't "precomputed"
                if algorithm == 'kmedoids':
                    model = KMedoids(n_clusters=k, metric="precomputed",
                                 random_state=random_state)
                    model.fit(data)
                #Metric used to compute the linkage. Can be “euclidean”, “l1”, “l2”, “manhattan”, “cosine”, or “precomputed”.
                #If linkage is “ward”, only “euclidean” is accepted. 
                #If “precomputed”, a distance matrix (instead of a similarity matrix) is needed as input for the fit method.
                #When "precomputed" was setted in affinity, linkage is unable to use "ward", so "average" is setted.
                if algorithm == 'hierarchical':
                    model = AgglomerativeClustering(n_clusters=k,affinity = 'precomputed',linkage = 'average')                
                    model.fit(data)
                    
                #Fit and return the result of each sample's clustering assignment.
                cluster_labels = model.fit_predict(data)
                silhouette_avg = silhouette_score(data, cluster_labels, metric = "precomputed")                                
            
            
            resultsdf = resultsdf.append({'algorithm':algorithm, 'clusterCount':k, 
                                          'silhouette':silhouette_avg}, ignore_index=True)
    
    algorithm1_df = resultsdf[resultsdf['algorithm']==algorithm1]
    algorithm2_df = resultsdf[resultsdf['algorithm']==algorithm2]
    
    return resultsdf


def neigh_dist(dissim, task='Implicit', rels = 159):
    """UMAP"""
    neighbors = [5,10,20,30]
    dists = [0.001, 0.01]

    umaps_results = pd.DataFrame(columns=['neighbor','distance','Dim1','Dim2'])
    for n in neighbors:
        for d in dists:
            temp_umap = umap.UMAP(n_neighbors=n, min_dist=d, n_components=2,
                                  random_state=random_seed,metric='precomputed').fit_transform(dissim)
            temp_umap = pd.DataFrame(temp_umap, columns=['Dim1','Dim2'])
            temp_umap['neighbor'] = n
            temp_umap['distance'] = d
            umaps_results = umaps_results.append(temp_umap, sort=True,ignore_index=True)
            
    # Create dataframe
    optimal_k_umap = pd.DataFrame()

    for dist in [0.001, 0.01]:
        for ngbr in [5,10,20,30]:
            df_subset = umaps_results[(umaps_results['distance']==dist) & (umaps_results['neighbor']==ngbr)].iloc[:,:2]
            temp_df = optimalK_grouped(data_type='df',data=df_subset, algorithm1='kmeans', algorithm2='hierarchical', 
                                       random_state=random_seed, title="test")
            temp_df['distance'] = dist
            temp_df['neighbor'] = ngbr

            optimal_k_umap = optimal_k_umap.append(temp_df, ignore_index=True)


    optimal_k_umap = optimal_k_umap.reset_index(drop=True)
    optimal_k_umap_hierarchical = optimal_k_umap[optimal_k_umap['algorithm']=='hierarchical']
    optimal_k_umap_kmeans = optimal_k_umap[optimal_k_umap['algorithm']=='kmeans']
    
    # Plot
    #f,axes = plt.subplots(2,1,figsize=(5,10))
    
    #Hierarchical clustering
    #sns.lineplot(data=optimal_k_umap_hierarchical, x="clusterCount", y="silhouette", hue="distance",
    #             style="neighbor", palette='colorblind',ax=axes[0])
    #axes[0].legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    #axes[0].set_title("Optimal Distance and Neighbor for " + task+ ""+ str(rels) + " Hierarchical Clustering", fontsize=8)
    #axes[0].scatter(optimal_k_umap_hierarchical.loc[optimal_k_umap_hierarchical['silhouette'].idxmax(),'clusterCount'],
    #                optimal_k_umap_hierarchical['silhouette'].max(),c='red')
    h_dist = optimal_k_umap_hierarchical.loc[optimal_k_umap_hierarchical['silhouette'].idxmax(),'distance']
    h_neigh = optimal_k_umap_hierarchical.loc[optimal_k_umap_hierarchical['silhouette'].idxmax(),'neighbor']
    
    #KMeans clustering
    sns.lineplot(data=optimal_k_umap_kmeans, x="clusterCount", y="silhouette", hue="neighbor",
             style="distance", palette='colorblind')
    plt.title("Optimal Distance and Neighbor for " + task+ ""+ str(rels) + " KMeans Clustering", fontsize=8)
    plt.scatter(optimal_k_umap_kmeans.loc[optimal_k_umap_kmeans['silhouette'].idxmax(),'clusterCount'],
                    optimal_k_umap_kmeans['silhouette'].max(),c='red')
    k_dist = optimal_k_umap_kmeans.loc[optimal_k_umap_kmeans['silhouette'].idxmax(),'distance']
    k_neigh = optimal_k_umap_kmeans.loc[optimal_k_umap_kmeans['silhouette'].idxmax(),'neighbor']
    
    #result_dict = {'hierarchical':optimal_k_umap_hierarchical,'kmeans':optimal_k_umap_kmeans,
    #               'h_parameter':[h_dist,h_neigh],'k_parameter':[k_dist,k_neigh]}
    result_dict = {'h_parameter':[h_dist,h_neigh],'k_parameter':[k_dist,k_neigh]}
    return(result_dict)


def perperlixty(dissim, task='Dimensional', rels = 159):
    """t-SNE"""
    tsne_model_p05 = TSNE(n_components=2, perplexity=5,
                     random_state=random_seed, metric='precomputed').fit_transform(dissim)
    tsne_model_p05 = pd.DataFrame(tsne_model_p05, columns=['Dim1','Dim2'],
                                  index=dissim.index)

    tsne_model_p10 = TSNE(n_components=2, perplexity=10,
                         random_state=random_seed, metric='precomputed').fit_transform(dissim)
    tsne_model_p10 = pd.DataFrame(tsne_model_p10, columns=['Dim1','Dim2'],
                                  index=dissim.index)


    # Create dataframe and attach data from first task
    optimal_k_tnse = optimalK_grouped(data_type='df',data=tsne_model_p05, algorithm1='kmeans', algorithm2='hierarchical', 
             random_state=random_seed, title="Optimal k for t-SNE Clustering")
    optimal_k_tnse['perplexity'] = 5


    # Add data from additional tasks
    temp_df = optimalK_grouped(data_type='df',data=tsne_model_p10, algorithm1='kmeans', algorithm2='hierarchical', 
             random_state=random_seed, title="Optimal k for t-SNE Clustering")
    temp_df['perplexity'] = 10
    optimal_k_tnse = optimal_k_tnse.append(temp_df, ignore_index=True)


    # Plot
    sns.lineplot(data=optimal_k_tnse, x="clusterCount", y="silhouette", hue="perplexity", 
                 style="algorithm", palette='colorblind')
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    plt.title("Optimal Perperlixty for "+task+" "+ str(rels)+ " Clustering", fontsize=15)
    
    return(plt)


def create_cluster_models(data_type, data, methods, ks, keep_orig=False):
    """Only use kmeans or kmedoids. Using both clustering methods will results in overwritten data. 
    Only kmeans will be returned"""
    
    ###############################################################################################
    ###When the Dissimilar Matrix is inputted in Clustering function,"precomputed" should be stated 
    ###############################################################################################   
    if data_type == 'dissim':
        clust_results = pd.DataFrame(index=data.index)
        for k in ks:
            for m in methods:
                if m == "KMedoids":
                    # KMedoids clustering
                    fit_cluster = KMedoids(n_clusters=k, metric='precomputed', 
                                              random_state=random_seed).fit(data)
                    # Cluster labels for each point.
                    clust_results['cl_k'+str(k)] = fit_cluster.labels_

                #Kmeans hasn't "precomputed"

                elif m == "Hierarchical":
                    # Hierarchical clustering
                    fit_cluster = AgglomerativeClustering(n_clusters=k,affinity = 'precomputed',linkage = 'average').fit(data)
                    clust_results['cl_h'+str(k)] = fit_cluster.labels_        

    if data_type == 'df':
        if keep_orig == True:
            clust_results = data.loc[:]
        else:
            clust_results = pd.DataFrame(index=data.index)

        for k in ks:
            for m in methods:
                if m == "KMedoids":
                    # KMedoids clustering
                    fit_cluster = KMedoids(n_clusters=k, metric='euclidean', 
                                              random_state=random_seed).fit(data)
                    clust_results['cl_k'+str(k)] = fit_cluster.labels_

                elif m == "KMeans":
                    # KMeans clustering
                    fit_cluster = KMeans(n_clusters=k, random_state=random_seed).fit(data)
                    clust_results['cl_k'+str(k)] = fit_cluster.labels_

                elif m == "Hierarchical":
                    # Hierarchical clustering
                    fit_cluster = AgglomerativeClustering(n_clusters=k,linkage = 'average').fit(data)
                    clust_results['cl_h'+str(k)] = fit_cluster.labels_

    return clust_results


def cluster_results(result_df, method_number='cl_k5'):
    for n in range(len(result_df[method_number].unique())):
        each_cluster = result_df.index[result_df[method_number]==n]
        print("\nCluster "+str(n+1)+" Relationship:{}".format(len(each_cluster)))
        print(*result_df.index[result_df[method_number]==n], sep = ", ")


def scatter_center_num(reduction_model,cluster_plot,cluster_model,k ,num):
    """
    Plot relationships distribution in 2-D space according to the corresponding cluster model
    Params:
        reduction_model: reduction results derived by t-SNE or UMAP reduction
        cluster_plot: cluster results
        cluster_model: the algorithm used and the optimal clusters setted
        k: the optimal clusters setted
        num: number of center relationships in each cluster
    Returns:(plot,silhouette(silhouette_dict_sorted)，
             center_rel_list，center_rel_dict)
    """
    plt.figure(figsize=(10,10))
    sns.scatterplot(data=cluster_plot,x='Dim1',y='Dim2',
                   hue=cluster_model,palette=sns.color_palette('deep',k))

    #for line in range(159):
    #     plt.text(cluster_plot['Dim1'][line],cluster_plot['Dim2'][line], s=cluster_plot.index[line],
    #             horizontalalignment='center', fontsize=8,
    #             color=sns.color_palette('deep',k)[cluster_plot[cluster_model][line]])



    # silhouette center x
    cluster_labels = KMeans(k, random_state=random_seed).fit_predict(reduction_model)
    silhouette_ind = silhouette_samples(reduction_model, cluster_labels)


    silhouette_df = pd.DataFrame({'relationship':reduction_model.index,
                                  'silhouette':silhouette_ind,
                                  'cluster_labels':cluster_labels})

    silhouette_dict = {'cluster'+str(num) : silhouette_df[silhouette_df['cluster_labels']==num] for num in range(k)}
    silhouette_dict_sorted = {}
    for cluster in silhouette_dict.keys():
        silhouette_dict_sorted[cluster] = silhouette_dict[cluster].sort_values(by='silhouette',ascending=False)


    selected_plot = []
    selected_dict = {}
    for cluster in silhouette_dict_sorted.keys():
        temp_df = silhouette_dict_sorted[cluster]
        temp_rel = list(temp_df['relationship'])
        rel_num = temp_rel[0:num]
        selected_dict[cluster] = rel_num
        selected_plot.append(rel_num)

    selected_plot = list(itertools.chain.from_iterable(selected_plot))


    new_texts = [plt.text(cluster_plot.loc[rel,'Dim1'],cluster_plot.loc[rel,'Dim2'],rel, fontsize=10,
                          color = sns.color_palette('deep',k)[cluster_plot.loc[rel,cluster_model]])
                          for rel in selected_plot]

    result_df = {}
    result_df['plot'] = adjust_text(new_texts, only_move={'text': 'y'})
    result_df['silhouette'] = silhouette_dict_sorted
    result_df['center_rel_list'] = selected_plot
    result_df['center_rel_dict'] = selected_dict
    return(result_df)

def silhouette_cluster(X, *n_cluster_list):
        for n_clusters in n_cluster_list:
            clusterer = KMeans(n_clusters=n_clusters, random_state=2022)
            cluster_labels = clusterer.fit_predict(X)

            silhouette_avg = silhouette_score(X, cluster_labels)
            sample_silhouette_values = silhouette_samples(X, cluster_labels)

            fig, (ax1, ax2) = plt.subplots(1, 2)
            fig.set_size_inches(18, 7)
            
            y_lower = 10
            for i in range(n_clusters):
                # Aggregate the silhouette scores for samples belonging to
                # cluster i, and sort them
                ith_cluster_silhouette_values = \
                    sample_silhouette_values[cluster_labels == i]

                ith_cluster_silhouette_values.sort()

                size_cluster_i = ith_cluster_silhouette_values.shape[0]
                y_upper = y_lower + size_cluster_i

                color = cm.nipy_spectral(float(i) / n_clusters)
                ax1.fill_betweenx(np.arange(y_lower, y_upper),
                                  0, ith_cluster_silhouette_values,
                                  facecolor=color, edgecolor=color, alpha=0.7)

                # Label the silhouette plots with their cluster numbers at the middle
                ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

                # Compute the new y_lower for next plot
                y_lower = y_upper + 10  # 10 for the 0 samples

            ax1.set_title("The silhouette plot for the various clusters.")
            ax1.set_xlabel("The silhouette coefficient values")
            ax1.set_ylabel("Cluster label")

            # The vertical line for average silhouette score of all the values
            ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

            ax1.set_yticks([])  # Clear the yaxis labels / ticks
            ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])


            # 2nd Plot showing the actual clusters formed
            colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
            ax2.scatter(X.iloc[:, 0], X.iloc[:, 1], marker='.', s=30, lw=0, alpha=0.7,
                        c=colors, edgecolor='k')

            # Labeling the clusters
            centers = clusterer.cluster_centers_
            # Draw white circles at cluster centers
            ax2.scatter(centers[:, 0], centers[:, 1], marker='o',
                        c="white", alpha=1, s=200, edgecolor='k')

            for i, c in enumerate(centers):
                ax2.scatter(c[0], c[1], marker='$%d$' % i, alpha=1,
                            s=50, edgecolor='k')

            ax2.set_title("The visualization of the clustered data.")
            ax2.set_xlabel("Feature space for the 1st feature")
            ax2.set_ylabel("Feature space for the 2nd feature")

            plt.suptitle(("Silhouette analysis for KMeans clustering on sample data "
                          "with n_clusters = %d" % n_clusters),
                         fontsize=14, fontweight='bold')
