#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

def master_tab(pdf, *arg):
    
    
    def weighted(cc,pdf):
        lis = []
        for i in cc:
            lis.append(pdf['V005'][i])

        return (sum(lis)/1000000)
    def single_tab(pdf, col):
        pdf = pdf[pdf[col].notna()]
        uniqueValues = pdf[col].unique()

        freq_lis = []
        for un in uniqueValues:
            cc = pdf[pdf[col]== un].index.tolist()
            freq_lis.append(weighted(cc,pdf))
        per_list =[]
        for fl in freq_lis:
            per_list.append(round((fl)/sum(freq_lis)*100, 1))

        return per_list

    def double_tab(data, var1, var2):
        data = data[data[var1].notna()]
        data = data[data[var2].notna()]
        uniqueValues_unlist = data[var1].unique()
        uniqueValues1_unlist = data[var2].unique()  
        uniqueValues_sorted = (uniqueValues_unlist.tolist())
        uniqueValues_sorted.sort()
        uniqueValues1_sorted = (uniqueValues1_unlist.tolist())
        uniqueValues1_sorted.sort()

        uniqueValues_Repitation =  [ele for ele in uniqueValues_sorted for i in range(len(uniqueValues1_sorted))] 
        uniqueValues1_Repitation = uniqueValues1_sorted * len(uniqueValues_sorted)

        freq_lis = []
        for j,k in zip(uniqueValues_Repitation,uniqueValues1_Repitation):
            cc = data[((data[var1] == j ) & (data[var2] == k))].index.tolist() 
            freq_lis.append(weighted(cc, data))

        my_tab = pd.crosstab(data[var1], data[var2])

        nc = len(my_tab.columns.tolist())
        yi = my_tab.index.tolist()

        listc = [freq_lis[i:i + nc] for i in range(0, len(freq_lis), nc)]


        b = 0
        for q in range(len(yi)):
            my_tab.iloc[q]=listc[b]
            b=b+1
        per_lis = round((my_tab.div(my_tab.sum(axis=1), axis=0) * 100),1)  
        return per_lis    
  
    if len(arg)==1:
        col = arg[0]
        return single_tab(pdf, col)
        
    elif len(arg)==2:
        var1 = arg[0]
        var2 = arg[1]
        return double_tab(pdf,var1,var2)

        
    elif len(arg)==0:
        print('Please insert the variable you want to tabulate ')
    else:
        print('This cross-tabulation is only work for two variable argument')

def per_table(data, ind , dep):
    tot_temp = []
    lo = []   
    for row in ind:
        
        for col in dep:
            
            temp = master_tab(data,row,col)
            del temp[0]
            temp.columns =[temp.columns.name]
            if col == dep[0]:
                tot_temp =temp
                continue
                
            tot_temp = tot_temp.join(temp)
        lo.append(tot_temp)
        y= lo[0].T
        del y[0]
        teb = y.T
        teb = teb.rename(index = {1.0:teb.index.name})
    if len(ind)>1 :
        for ap in range(len(ind)-1):
            z= lo[ap+1].T
            del z[0]
            tab_tem = z.T
            tab_tem = tab_tem.rename(index = {1.0:tab_tem.index.name})
            teb =teb.append(tab_tem)
    return teb


