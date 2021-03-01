#!/usr/bin/env python
# coding: utf-8

# In[3]:



import numpy as np
import pandas as pd
from tabu import master_tab

class CM:
    def __init__(self, data, meta,data_type, year,precd):
        self.data = data
        self.meta = meta
        self.year = year
        self.precd= precd
        self.data_type= data_type
        #self.table = table
 
    def child_mortality(self):
        if self.year==2000:
            self.data.columns = self.data.columns.str.upper()       
        df_child_mr = self.data.copy()
        b3,b5,b7,cm_list = [],[],[],[]
        if self.data_type == 'IR':
            for i in range(20):
                if i<9:
                    b3.append('B3_0'+str(i+1)), b5.append('B5_0'+str(i+1)), b7.append('B7_0'+str(i+1))
                else:
                    b3.append('B3_'+str(i+1)), b5.append('B5_'+str(i+1)), b7.append('B7_'+str(i+1))
            b=b3+b5+b7
            cm_list = ['V005','V013','V024','V025','V106','V190','V008']+b
            df_child_mr.drop(df_child_mr.columns.difference(cm_list), 1, inplace=True)
            #df_child_mr = df_child_mr.fillna(-999)
            childm = ['NNM', 'IM','PNM','CM','U5M']  
            for varx in childm:
                df_child_mr[varx] =0

            if self.precd == 5 :ty = 60 ; tx = 0
            if self.precd == 10 :ty = 120 ; tx = 60
            if self.precd == 15 :ty = 120 ; tx = 180 
            df_child_mr['t1'] = df_child_mr['V008']  - ty
            df_child_mr['t2'] =df_child_mr['V008'] -tx
            ty = 0
            tx = 0
            col_name = childm
            if self.year==2000:
                 bcar = ['V013','V025','V024','V106']
            else:
                bcar = ['V013','V025','V024','V106','V190']
            li_temp = []
            lo =[]

            for j in range(20):
                df_child_mr['NNM'].loc[(df_child_mr[b5[j]]==0)&(df_child_mr[b7[j]]<1)&(df_child_mr[b3[j]]>df_child_mr['t1'])&(df_child_mr[b3[j]]<df_child_mr['t2'])]=1     
                df_child_mr['IM'].loc[(df_child_mr[b5[j]]==0)&(df_child_mr[b7[j]]<12)&(df_child_mr[b3[j]]>df_child_mr['t1'])&(df_child_mr[b3[j]]<df_child_mr['t2'])]=1     
                df_child_mr['PNM'].loc[(df_child_mr[b5[j]]==0)&(df_child_mr[b7[j]]>0)&(df_child_mr[b7[j]]<12)&(df_child_mr[b3[j]]>df_child_mr['t1'])&(df_child_mr[b3[j]]<df_child_mr['t2'])]=1     
                df_child_mr['CM'].loc[(df_child_mr[b5[j]]==0)&(df_child_mr[b7[j]]>11)&(df_child_mr[b7[j]]<60)&(df_child_mr[b3[j]]>df_child_mr['t1'])&(df_child_mr[b3[j]]<df_child_mr['t2'])]=1     
                df_child_mr['U5M'].loc[(df_child_mr[b5[j]]==0)&(df_child_mr[b7[j]]<60)&(df_child_mr[b3[j]]>df_child_mr['t1'])&(df_child_mr[b3[j]]<df_child_mr['t2'])]=1     
        
        elif self.data_type == 'BR':
            cm_list = ['V005','V013','V024','V025','V106','V190','V008','B5','B7','B3']
            df_child_mr.drop(df_child_mr.columns.difference(cm_list), 1, inplace=True)
            #df_child_mr = df_child_mr.fillna(-999)
            childm = ['NNM', 'IM','PNM','CM','U5M']  
            for varx in childm:
                df_child_mr[varx] =0

            if self.precd == 5 :ty = 60 ; tx = 0
            if self.precd == 10 :ty = 120 ; tx = 60
            if self.precd == 15 :ty = 120 ; tx = 180 
            df_child_mr['t1'] = df_child_mr['V008']  - ty
            df_child_mr['t2'] =df_child_mr['V008'] -tx
            ty = 0
            tx = 0
            col_name = childm
            if self.year==2000:
                 bcar = ['V013','V025','V024','V106']
            else:
                bcar = ['V013','V025','V024','V106','V190']
            li_temp = []
            lo =[]

            for j in range(20):
                df_child_mr['NNM'].loc[(df_child_mr['B5']==0)&(df_child_mr['B7']<1)&(df_child_mr['B3']>df_child_mr['t1'])&(df_child_mr['B3']<df_child_mr['t2'])]=1     
                df_child_mr['IM'].loc[(df_child_mr['B5']==0)&(df_child_mr['B7']<12)&(df_child_mr['B3']>df_child_mr['t1'])&(df_child_mr['B3']<df_child_mr['t2'])]=1     
                df_child_mr['PNM'].loc[(df_child_mr['B5']==0)&(df_child_mr['B7']>0)&(df_child_mr['B7']<12)&(df_child_mr['B3']>df_child_mr['t1'])&(df_child_mr['B3']<df_child_mr['t2'])]=1     
                df_child_mr['CM'].loc[(df_child_mr['B5']==0)&(df_child_mr['B7']>11)&(df_child_mr['B7']<60)&(df_child_mr['B3']>df_child_mr['t1'])&(df_child_mr['B3']<df_child_mr['t2'])]=1     
                df_child_mr['U5M'].loc[(df_child_mr['B5']==0)&(df_child_mr['B7']<60)&(df_child_mr['B3']>df_child_mr['t1'])&(df_child_mr['B3']<df_child_mr['t2'])]=1 

            
        for var_bc in bcar:
                   
            for var_col in col_name:
              
                frm_temp=master_tab(df_child_mr,var_bc,var_col)
                if self.year ==2000:
                    var_bc= var_bc.lower()             
                frm_temp.index =list((self.meta.value_labels[var_bc]).values())
                frm_temp.index.name= self.meta.column_names_to_labels[var_bc]
                var_bc= var_bc.upper()
                del frm_temp[0]
                    #print(frm_temp.columns.values)
                frm_temp.columns =[frm_temp.columns.name]
                if var_col == col_name[0]:
                    li_temp = frm_temp
                    continue
                li_temp = li_temp.join(frm_temp)
            p = li_temp.index.name
            li_temp.loc[p]=''
            newIndex=[p]+[ind for ind in li_temp.index if ind!=p]
            li_temp=li_temp.reindex(index=newIndex)
            lo.append(li_temp)
        if self.year ==2000:
            final_table =(((lo[0].append(lo[1])).append(lo[2])).append(lo[3]))
        else:
            final_table =(((lo[0].append(lo[1])).append(lo[2])).append(lo[3])).append(lo[4])
        final_table.index.name = 'Background characterstics'
        fil_col=['Neonatal mortality','Infant mortality','Post neonatal mortality','Child mortality','Under-five mortality']
        final_table.columns = fil_col
           
        return final_table,df_child_mr




# In[1]:


b9 = 'B9'
b10 = 'B10'
b =b9+b10


# In[2]:


b


