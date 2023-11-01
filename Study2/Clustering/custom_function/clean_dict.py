# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import manifold, preprocessing
import warnings

"""
clean_data: separate different parts from all items 
combine_data: combine data in three versions into one whole response
dict_data: organize data into dictionary
"""

warnings.filterwarnings('ignore')
#relationship list
relationships = pd.read_csv('../input_data/159relationships_fix_label.csv', index_col = 0)
relationships = list(relationships.iloc[:,0])

#dimension list
key = pd.read_csv('../input_data/credamo_question_key.csv')


def clean_data(vnum,region,Qstart,Qend):
    """
    separate different parts from all items
    parameter:
        vnum: the version of survey
        region: data collecting in region / country
        Qstart,Qend: control the item index of main questions

    output:
        'main': main part of questions
        'dim_com': comprehension of dimensions
        'rel_size': check items
        'familiarity': familiarity of relationships rated
    """
    result_df = {}
    #import data
    file_path = '../input_data/'+region+'/'+region+'_'+str(vnum)+'.csv'
    raw_data = pd.read_csv(file_path,index_col=None, header=1,encoding='UTF-8')
    #drop 'suggestion'
    raw_reorg = raw_data.drop(['Q42'], axis=1)
    raw_reorg['subject'] = list(raw_reorg.index)
    raw_reorg = raw_reorg.reset_index(drop=True)
    
    response = raw_reorg
    response['subject'] = list(raw_reorg.index)
    response = response.loc[:,response.columns.str.startswith('Q')]
    
    
    #Questionnaires
    #main question:V1,Q4-14;V2,Q15-Q25;V3,Q26-Q33,Q35-Q36,Q38
    count = Qstart
    filtered_main = []
    while count <= Qend:
        [filtered_main.append(col) for col in raw_reorg if col.startswith('Q'+str(count)+'_2')]
        if count == 33 or count == 36:
            count = count + 2
        else:
            count += 1
    response_main = response[filtered_main]

    #check_rel_size:Q39,Q40
    filtered_rel_size = [col for col in raw_reorg if (col.startswith('Q39'))|(col.startswith('Q40'))]
    response_rel_size = response[filtered_rel_size]
    
    #familiarity: Q0
    filtered_familiarity = [col for col in raw_reorg if (col.startswith('Q0'))]
    response_familiarity = response[filtered_familiarity]

    #dim_comprehension
    count = Qstart
    filtered_dim_com = []
    while count <= Qend:
        [filtered_dim_com.append(col) for col in raw_reorg if col.startswith('Q'+str(count)+'_1')]
        if count == 33 or count == 36:
            count += 2
        else:
            count += 1
    response_dim_com = response[filtered_dim_com]        

    #output
    result_df['main'] = response_main
    result_df['dim_com'] = response_dim_com
    result_df['rel_size'] = response_rel_size
    result_df['familiarity'] = response_familiarity
    return result_df



data_type = ['main','dim_com','rel_size','familiarity']
def combine_data(region,*data_type):
    """
    combine data in three versions into one whole response
    parameter:
        region: data collecting in region / country
        data_type = ['main','dim_com','rel_size','familiarity']

    output:
        the same as clean_data()
    """
    result_df = {}
    vnum_list = [1,2,3]
    Qstart_list = [4,15,26]
    Qend_list = [14,25,38]

    for data in data_type:
        for vnum,Qstart,Qend in zip(vnum_list,Qstart_list,Qend_list):
            if vnum == 1:
                all_data = clean_data(vnum,region,Qstart,Qend)[data]

            else:   
                temp = clean_data(vnum,region,Qstart,Qend)[data]
                all_data = pd.concat([all_data,temp])
        result_df[data] = all_data

    return result_df    


def dict_data(region,vnum,response,foils_rel_size,familiarity,
              detail_pre=False,detail_after=False):
    """
    organize data into dictionary
    parameter:
        vnum: the version of survey(1~3 / 'all')
        response,foils_rel_size,familiarity: the results of clean_data()
        detail_pre: statistics of the number of people and the amount of data
        detail_after: the same as above but that after filtering based on check and familarity items

    output:
        dimension_frames_outliers(dictionary)
    """
    
    ###### all raw data ######
    response = response.reset_index(drop=True)
    dimensions = key['dimension'].tolist()[1:34]
    if vnum == 1:
        dimensions = dimensions[0:11]
        count = 4
    elif vnum == 2:
        dimensions = dimensions[11:22]
        count = 15
    elif vnum == 3:
        dimensions = dimensions[22:33]
        count = 26
    elif vnum == 'all':
        count = 4
    dimension_frames = {}

    for dim in dimensions:  # exclude foil and demographics ## change this variable
        filtered_cols = [col for col in response if col.startswith('Q'+str(count)+'_2')] ## change this variable 
        dimension_frames[dim] = pd.DataFrame(response[filtered_cols])
        dimension_frames[dim].columns = relationships
        if count == 33 or count == 36:
            count = count +2
        else:
            count = count+1
    
    num_response = pd.DataFrame(columns=dimensions)
    for dim in dimensions:
        num_response[dim] = dimension_frames[dim].count() 
    
    if detail_pre:
        print("Total number of relationships - " + str(len(dimension_frames[dim].columns)))
        print("Total number of dimensions - " + str(len(dimensions)))

        '''Check total number of responses for each word
        '''

        print("Total number of responses, including all participants - "+str(len(dimension_frames[dim])))
        print("Smallest number of ratings for a relationship - " + str(min(list(num_response.min()))))
        print("Largest number of ratings for a relationship - " + str(max(list(num_response.max()))))
    
    
    ###### Attention question check ######
    '''Attention question check
    '''
    foil_items = pd.read_csv('../input_data/attention_key.csv', index_col=None, header=None)
    foils_rel_size = foils_rel_size.reset_index(drop=True)
    foils_rel_size.columns = foil_items.iloc[0,:]
    foils_rel_size['subject'] = foils_rel_size.index.to_list()
    foils_rel_size = foils_rel_size.apply(pd.to_numeric)
    foils_rel_size_melt = pd.melt(foils_rel_size, id_vars='subject')
    foils_rel_size_melt.columns = ['subject','variable','value']

    outliers_rel_size_list = []
    for col in foils_rel_size.columns[:-1]:
        outliers_rel_size_list = outliers_rel_size_list + list(foils_rel_size[(foils_rel_size[col] > 
                       foils_rel_size[col].mean()+foils_rel_size[col].std()*3.5) |
                       (foils_rel_size[col] < 
                        foils_rel_size[col].mean()-foils_rel_size[col].std()*3.5)].index)
    outliers_rel_size_list = set(outliers_rel_size_list)

    foil_rel_size_outliers = foils_rel_size
    foil_rel_size_outliers = foil_rel_size_outliers[~foil_rel_size_outliers.index.isin(outliers_rel_size_list)]
    foil_rel_size_outliers_melt = pd.melt(foil_rel_size_outliers, id_vars='subject')
    foil_rel_size_outliers_melt.columns = ['subject','variable','value']
    
    f, axes = plt.subplots(2, 1, figsize=(18, 7), sharex=False)
    sns.despine(left=True)
    sns.stripplot(x="variable", y="value", data=foils_rel_size_melt, 
                  color='.3', jitter=True, ax=axes[0])
    sns.stripplot(x="variable", y="value", data=foil_rel_size_outliers_melt, 
                  color='.3', jitter=True,  ax=axes[1])
    sns.boxplot(x="variable", y="value", data=foils_rel_size_melt, whis=np.inf, ax=axes[0])
    sns.boxplot(x="variable", y="value", data=foil_rel_size_outliers_melt, whis=np.inf, ax=axes[1])
    plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.0)

    #check familiarity
    familiarity = familiarity.reset_index(drop=True)
    familiarity.columns = relationships
    familiarity['subject'] = familiarity.index.to_list()
    familiarity = familiarity.apply(pd.to_numeric)
    familiarity_melt = pd.melt(familiarity, id_vars='subject')

    #Check for values above means for unexpected foils
    familiarity_list = []
    for col in familiarity.columns[:-1]:
        familiarity_list = familiarity_list + list(familiarity[(familiarity[col] > 
                       familiarity[col].mean()+familiarity[col].std()*3.5) |
                       (familiarity[col] < 
                        familiarity[col].mean()-familiarity[col].std()*3.5)].index)
    familiarity_list = set(familiarity_list)

    #remove outliers from original data
    outliers_all_list = set(list(outliers_rel_size_list) + list(familiarity_list))
    outliers_all_list_df = pd.DataFrame(outliers_all_list)
    outliers_all_list_df.to_csv('../output_data/outlier_df/'+region+'.csv')
    dimension_frames_outliers = dimension_frames.copy()
    for dim in dimension_frames_outliers:
        dimension_frames_outliers[dim] = dimension_frames[dim][~dimension_frames[dim].index.isin(outliers_all_list)]
        dimension_frames_outliers[dim] = dimension_frames_outliers[dim].apply(pd.to_numeric)

    #Check total number of responses for each word with outliers excluded
    num_response_outliers = pd.DataFrame(index=relationships,columns=dimensions)
    for dim in dimensions:
        num_response_outliers[dim] = dimension_frames_outliers[dim].count() 
#
    if detail_after:
        print("Total number of responses, excluding bad participants - "+str(len(dimension_frames_outliers[dim])))
        print("Smallest number of ratings for a relationship - " + str(min(list(num_response_outliers.min()))))
        print("Largest number of ratings for a relationship - " + str(max(list(num_response_outliers.max()))))
    
    return dimension_frames_outliers
