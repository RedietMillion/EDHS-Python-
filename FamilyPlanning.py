#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
from tab import master_tab

class FP:
    def __init__(self, data, meta, year):
        self.data = data
        self.meta = meta
        self.year = year
        #self.table = table

    def know_contra(self,table):
    # Preprocessing of data
        kc_col = ['V312','V313','V005','V502','V301','V528','V304_06','V304_07','V304_01','V304_02','V304_03','V304_11','V304_05','V304_14','V304_16','V304_18', 'V304_13','V304_17','V304_08','V304_09','V304_10','V013','V024','V025','V106','V190']
        data_know = self.data.copy()
        data_know.drop(data_know.columns.difference(kc_col), 1, inplace=True)
        data_know = data_know.fillna(-999)
    #----------------------------------------------------------------------------------
        fp_knw = ['Any method', 'Female sterilisation','Male sterilisation','Pill','IDU','Injectables','Implants', 'Male condom','Female condom','Emergency contraception','SDM','LAM','Other modern method','Rhythm','Withdrawal','Other','Any traditional method','Any modern method']
        for varx in fp_knw:
            data_know[varx] =0   

        #Knowledge of contraceptive methods
        if table == 'table7_1':
            knw_sf = ['Any method', 'Female sterilisation','Male sterilisation','Pill','IDU','Injectables','Implants', 'Male condom','Female condom','Emergency contraception','SDM','LAM','Other modern method','Rhythm','Withdrawal','Other','Any traditional method','Any modern method']
            var_cont= ['V301','V304_06','V304_07','V304_01','V304_02','V304_03','V304_11','V304_05','V304_14','V304_16','V304_18', 'V304_13','V304_17','V304_08','V304_09','V304_10']

            for j in range(len(knw_sf)-2):
                data_know[knw_sf[j]].loc[((data_know[var_cont[j]]>=1)&(data_know[var_cont[j]]<8))] = 1

            data_know['Any modern method'].loc[(data_know['V301']==3)] = 1
            data_know['Any traditional method'].loc[((data_know['Rhythm']==1)|(data_know['Withdrawal']==1)|(data_know['Other']==1))] = 1

            tab1 = []
            tab2 = []
            tab3=[]
            fr =[]
            if self.year==2011:
                knw_sft1 = ['Any method','Any modern method', 'Female sterilisation','Male sterilisation','Pill','IDU','Injectables','Implants', 'Male condom','Female condom','Emergency contraception','SDM','LAM','Any traditional method','Rhythm','Withdrawal','Other']
            elif self.year ==2016:
                knw_sft2 = ['Any method','Any modern method', 'Female sterilisation','Male sterilisation','Pill','IDU','Injectables','Implants', 'Male condom','Female condom','Emergency contraception','SDM','LAM','Other modern method','Any traditional method','Rhythm','Withdrawal','Other']


            col= ['All women','Currently married women','sexually active unmarried women']
            data_know2 =data_know.copy()
            for cl in col:
                if cl=='All women':
                    if self.year ==2011:
                        for out in  range(len(knw_sft1)):
                            if out<=8:
                                if((knw_sft1[out]=='IDU')|(knw_sft1[out]=='Any traditional method')|(knw_sft1[out]=='Rhythm')):tab1.append(master_tab(data_know,knw_sft1[out])[1])
                                else:tab1.append(master_tab(data_know,knw_sft1[out])[0])     
                            else:
                                if((knw_sft1[out]=='IDU')|(knw_sft1[out]=='Any traditional method')|(knw_sft1[out]=='Rhythm')):tab1.append(master_tab(data_know,knw_sft1[out])[0]) 
                                else: tab1.append(master_tab(data_know,knw_sft1[out])[1])

                    elif self.year==2016:
                        for out in  range(len(knw_sft2)):
                            if out<=8:tab1.append(master_tab(data_know,knw_sft2[out])[0])
                            else:tab1.append(master_tab(data_know,knw_sft2[out])[1])

                    fr.append(pd.DataFrame(tab1,columns=[cl]))

                elif cl== 'Currently married women':
                    for v in knw_sf:
                        data_know[v].loc[((data_know['V502']!=1))] = np.nan
                    if self.year ==2011:
                        for out in  range(len(knw_sft1)):
                            if out<=8:
                                if((knw_sft1[out]=='IDU')|(knw_sft1[out]=='Any traditional method')|(knw_sft1[out]=='Rhythm')):tab2.append(master_tab(data_know,knw_sft1[out])[1])
                                else:tab2.append(master_tab(data_know,knw_sft1[out])[0])     
                            else:
                                if((knw_sft1[out]=='IDU')|(knw_sft1[out]=='Any traditional method')|(knw_sft1[out]=='Rhythm')):tab2.append(master_tab(data_know,knw_sft1[out])[0]) 
                                else: tab2.append(master_tab(data_know,knw_sft1[out])[1])

                    elif self.year==2016:
                        for out in  range(len(knw_sft2)):
                            if out<=8:tab2.append(master_tab(data_know,knw_sft2[out])[0])
                            else:tab2.append(master_tab(data_know,knw_sft2[out])[1])

                    fr.append(pd.DataFrame(tab2,columns=[cl]))

                elif cl== 'sexually active unmarried women':
                    data_know2['select']=0
                    data_know2['select'].loc[((self.data['V502']!=1) & (self.data['V528']<=30))] =1
                    if self.year ==2011:
                        for out in  range(len(knw_sft1)):
                            if out<=8:
                                if((knw_sft1[out]=='IDU')|(knw_sft1[out]=='Any traditional method')|(knw_sft1[out]=='Rhythm')):tab3.append(master_tab(data_know,knw_sft1[out])[1])
                                else:tab3.append(master_tab(data_know,knw_sft1[out])[0])     
                            else:
                                if((knw_sft1[out]=='IDU')|(knw_sft1[out]=='Any traditional method')|(knw_sft1[out]=='Rhythm')):tab3.append(master_tab(data_know,knw_sft1[out])[0]) 
                                else: tab3.append(master_tab(data_know,knw_sft1[out])[1])

                    elif self.year==2016:
                        for out in  range(len(knw_sft2)):
                            if out<=8:tab3.append(master_tab(data_know,knw_sft2[out])[0])
                            else:tab3.append(master_tab(data_know,knw_sft2[out])[1])

                    fr.append(pd.DataFrame(tab3,columns=[cl]))


            final_table= (fr[0].join(fr[1])).join(fr[2])
            if self.year ==2011:
                 final_table.index= knw_sft1
            elif self.year ==2016:
                final_table.index= knw_sft2

            final_table.index.name = 'Methods'
            #final_table=tab3

        # Knowledge of contraceptive methods according to background characteristics
        elif table=='table7_2':
            col_name = ['Any method','Any modern method']
            bcar = ['V013','V025','V024','V106','V190' ]
            li_temp = []

            for var_bc in bcar:
                data_know['Any modern method'].loc[(data_know['V301']==3)] = 1
                data_know['Any modern method'].loc[(data_know['V502']!=1)] = np.nan
                data_know['Any method'].loc[((data_know['V301']>=1)&(data_know['V301']<8))] = 1
                data_know['Any method'].loc[(data_know['V502']!=1)] = np.nan
                for var_col in col_name:
                    frm_temp=master_tab(data_know,var_bc,var_col)
                    frm_temp.index =list((self.meta.value_labels[var_bc]).values())
                    frm_temp.index.name= self.meta.column_names_to_labels[var_bc]
                    del frm_temp[0]
                    frm_temp.columns =[frm_temp.columns.name]
                    li_temp.append(frm_temp) 
            lo =[]
            for h in  range(len(li_temp)-1):
                j=1+h
                if li_temp[h].index.name == li_temp[j].index.name:
                    temp = li_temp[h].join(li_temp[j]) 
                    temp.index.name = li_temp[h].index.name
                    p = temp.index.name
                    temp.loc[p]=''
                    newIndex=[p]+[ind for ind in temp.index if ind!=p]
                    temp=temp.reindex(index=newIndex)
                    lo.append(temp)
            final = lo[0]
            for ap in range(len(lo)-1) :
                final = final.append(lo[ap+1])
            final_table =final
            final_table.index.name = 'Background characterstics'

        return final_table,data_know
    
    def curuse_contra(self,table):
        if self.year==2000:
            self.data.columns = self.data.columns.str.upper()
        # Preprocessing of self.data
        cu_col =  ['V013','V024','V025','V106','V190','V502', 'V528', 'V005','V312','V313','V219','V326']
        data_curuse = self.data.copy()
        data_curuse.drop(data_curuse.columns.difference(cu_col), 1, inplace=True)
        data_curuse = data_curuse.fillna(-999)
        #----------------------------------------------------------------------------------
        fp_curuse = ['Any method','Any modern method','Female sterilisation','Pill','IDU','Injectables','Implants', 'Other','Any traditional method','Rhythm','Withdrawal','Not currenlty using','Male condom','Emergency contraception','SDM','LAM'] 
        for varx in fp_curuse:
            data_curuse[varx] =0   
        def my_recode(row):
            
            if row == 0: return '0'
            elif (row==1)|(row==2): return '1-2'
            elif (row==3)|(row==4): return '3-4'
            elif row>=5: return '5+'
            
        data_curuse['Number of living children'] = data_curuse['V219'].apply(my_recode)
        
        if ((table=='table7_3')|(table=='table7_2')|(table=='table5_4')|(table=='table5_5_2000')):
            col_name = ['Any method','Any modern method','Female sterilisation','Pill','IDU','Injectables','Implants','Rhythm','Withdrawal','Not currenlty using','Male condom','Emergency contraception','SDM','LAM','Any traditional method','Other']
            bcar = ['V013','V013','V013']
            var_curr= [6 , 1, 2, 3, 11, 8, 9, 0,5,16,18,13 ]
            
            li_temp = [] 
            lo =[]
            i = 0
            status ={0:'ALL WOMEN', 1:'CURRENTLY MARRIED WOMEN',2:'SEXUALLY ACTIVE UNMARRIED WOMEN'}
            for var_bc in bcar:
                data_curuse['Any method'].loc[((data_curuse['V313']>0)&(data_curuse['V313']<8))] = 1
                data_curuse['Any modern method'].loc[(data_curuse['V313']==3)] = 1
                for j in range(len(var_curr)):
                    data_curuse[col_name[j+2]].loc[(data_curuse['V312']==var_curr[j])] = 1
                data_curuse['Any traditional method'].loc[((data_curuse['V313']>0)&(data_curuse['V313']<3))] = 1
                data_curuse['Other'] =data_curuse['Male condom']+data_curuse['Emergency contraception']+data_curuse['SDM']+ data_curuse['LAM']
                
                if i == 0 :
                    pass
                elif i==1:
                    for mar in col_name:
                        data_curuse[mar].loc[(data_curuse['V502']!=1)] = np.nan      
                elif i==2:
                    for mar in col_name:
                        data_curuse[mar].loc[((data_curuse['V502']!=1) & (data_curuse['V528']<=30))] = np.nan
                
            
                for var_col in col_name:
                    if ((self.year ==2011)|(self.year ==2005)|(self.year ==2000))&((var_col=='Emergency contraception')|(var_col=='SDM')|(var_col=='LAM')):
                        #print(var_col)
                        continue
                    else:
                        frm_temp=master_tab(data_curuse,var_bc,var_col)
                        if self.year ==2000:
                            var_bc= var_bc.lower()
                        frm_temp.index =list((self.meta.value_labels[var_bc]).values())
                        frm_temp.index.name= status[i]
                        var_bc= var_bc.upper()
                        del frm_temp[0]
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
                i=i+1
            final_table =((lo[0].append(lo[1])).append(lo[2]))
            final_table.index.name = 'Age'
         
        # Knowledge of contraceptive methods according to background characteristics
        if((table=='table7_4')|(table=='table7_3')|(table=='table5_5')|(table=='table5_6_1')):
            col_name = ['Any method','Any modern method','Female sterilisation','Pill','IDU','Injectables','Implants','Rhythm','Withdrawal','Not currenlty using','Male condom','Emergency contraception','SDM','LAM','Any traditional method','Other']
            if self.year==2000:
                 bcar = ['V025','V024','V106','Number of living children']
            else:
                bcar = ['Number of living children','V025','V024','V106','V190' ]
            var_curr= [6 , 1, 2, 3, 11, 8, 9, 0,5,16,18,13 ]
            
            li_temp = [] 
            lo =[]
            for var_bc in bcar:
                data_curuse['Any method'].loc[((data_curuse['V313']>0)&(data_curuse['V313']<8))] = 1
                data_curuse['Any modern method'].loc[(data_curuse['V313']==3)] = 1
                for j in range(len(var_curr)):
                    data_curuse[col_name[j+2]].loc[(data_curuse['V312']==var_curr[j])] = 1
                data_curuse['Any traditional method'].loc[((data_curuse['V313']>0)&(data_curuse['V313']<3))] = 1
                data_curuse['Other'] =data_curuse['Male condom']+data_curuse['Emergency contraception']+data_curuse['SDM']+ data_curuse['LAM']
                for mar in col_name:
                    data_curuse[mar].loc[(data_curuse['V502']!=1)] = np.nan
                
                for var_col in col_name:
                    if ((self.year ==2011)|(self.year ==2005)|(self.year ==2000))&((var_col=='Emergency contraception')|(var_col=='SDM')|(var_col=='LAM')):
                        continue
                    else:
                        frm_temp=master_tab(data_curuse,var_bc,var_col)
                        if self.year ==2000:
                            if var_bc =='Number of living children':
                                pass
                            else:
                                var_bc= var_bc.lower()
                                if ((var_bc =='v013')|(var_bc =='v025')|(var_bc =='v024')|(var_bc =='v106')):
                                    frm_temp.index =list((self.meta.value_labels[var_bc]).values())
                                    frm_temp.index.name= self.meta.column_names_to_labels[var_bc]
                                    var_bc= var_bc.upper()
                        else:        
                            if ((var_bc =='V025')|(var_bc =='V024')|(var_bc =='V106')|(var_bc =='V190')):
                                frm_temp.index =list((self.meta.value_labels[var_bc]).values())
                                frm_temp.index.name= self.meta.column_names_to_labels[var_bc]
                                
                        del frm_temp[0]
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
            if self.year==2000:
                final_table =(((lo[0].append(lo[1])).append(lo[2])).append(lo[3]))
            else:
                final_table =(((lo[0].append(lo[1])).append(lo[2])).append(lo[3])).append(lo[4])
            final_table.index.name = 'Background characterstics'
            
        return final_table,data_curuse
#-----------------------------------------------------------------------------------------------------------------------        
        
    def source_contra(self, table):
        if self.year==2000:
            self.data.columns = self.data.columns.str.upper()
        # Preprocessing of data
        so_col =  ['V013','V024','V025','V106','V190','V502', 'V528', 'V005','V312','V313','V219','V326']
        data_source = self.data.copy()
        data_source.drop(data_source.columns.difference(so_col), 1, inplace=True)
        data_source = data_source.fillna(-999)
        
        fp_source = ['Female sterilisation','Male condom','Pill','IDU','Injectables','Implants', 'Total','Condom']     
        for varx in fp_source:
            data_source[varx] =0   
        if((table=='table7_4')|(table=='table7_5')|(table=='table5_10')|(table=='table5_13')):
            if self.year==2011:
                col_name = ['Male condom','Pill','IDU','Injectables','Implants','Total']
                var_curr= [5 , 1, 2, 3, 11] 
            elif self.year==2016:
                col_name = ['Female sterilisation','Pill','IDU','Injectables','Implants','Total']
                var_curr= [6 , 1, 2, 3, 11] 
            elif self.year ==2005:
                col_name = ['Pill','IDU','Injectables','Condom']
                var_curr= [1 , 2, 3, 5] 
            elif self.year ==2000:
                col_name = ['Pill','IDU','Injectables','Condom']
                var_curr= [1 , 2, 3, 5] 
              
            li_temp = []     
     
            data_source['V326'].loc[(data_source['V326']==-999)] = np.nan  
            for j in range(len(var_curr)):
                data_source[col_name[j]].loc[(data_source['V312']==var_curr[j])] = 1
            
            data_source['Total'] = data_source[col_name[0]] + data_source['Pill']+data_source['IDU']+data_source['Injectables']+data_source['Implants']
            
            for var_col in col_name:
                frm_temp=master_tab(data_source,var_col,'V326').T
                del frm_temp[0]
                tem = frm_temp.T
                if self.year ==2011:
                    tem[10] = tem[11]+tem[12]+tem[13]+tem[14]+tem[15]
                    tem[20] = tem[21]+tem[22]+tem[23]+tem[24]+tem[25]
                    tem[30] = tem[31]+tem[32]+tem[96]+tem[99]
                elif self.year==2016:
                    tem[10] = tem[11]+tem[12]+tem[13]+tem[14]+tem[16]
                    tem[20] = tem[21]+tem[26]
                    tem[30] = tem[31]+tem[32]+tem[33]+tem[36]
                    tem[40] = tem[41]+tem[42]+tem[96]+tem[98]
                elif self.year==2005:
                    tem[10] = tem[11]+tem[12]+tem[13]+tem[14]+tem[15]+tem[16]
                    tem[20] = tem[21]+tem[22]+tem[23]
                    tem[24] = tem[25]+tem[26]
                    tem[30] = tem[31]+tem[32]+tem[33]
                elif self.year ==2000:
                    tem[10] = tem[11]+tem[12]+tem[13]+tem[14]+tem[15]+tem[16]
                    tem[20] = tem[21]+tem[22]+tem[23]
                    tem[24] = tem[25]+tem[26]
                    tem[30] = tem[31]+tem[32]+tem[33]+tem[95]    
                    
                #tem[40] = tem[41]+tem[42]+tem[96]+tem[98]
                frm_temp = tem.T
                frm_temp=frm_temp.sort_index(ascending=True)
                if self.year == 2000:
                    lst= list((self.meta.value_labels['v326']).values())
                    lst = lst[:len(lst)-1]
                    frm_temp.index = lst
                    
                elif self.year == 2005:
                    lst= list((self.meta.value_labels['V326']).values())
                    lst = lst[:len(lst)-2]
                    frm_temp.index = lst
                else:
                    frm_temp.index =list((self.meta.value_labels['V326']).values())
                if self.year==2000:
                    frm_temp.index.name= self.meta.column_names_to_labels['v326']
                else:
                    frm_temp.index.name= self.meta.column_names_to_labels['V326']
                    
                frm_temp.columns =[frm_temp.columns.name]
                if var_col == col_name[0]:
                    li_temp = frm_temp
                    continue
                li_temp = li_temp.join(frm_temp) 
            final_table =li_temp
            final_table.index.name = 'Source'
        else:
            return 'There is only one table for this topic!'
        
        return final_table,data_source
#-------------------------------------------------------------------------------------------------------------------------------

    def informed_choice(self, table):
        if self.year==2000:
            self.data.columns = self.data.columns.str.upper()
        # Preprocessing of data
        in_col =  ['V013','V024','V025','V106','V190','V502', 'V528', 'V005','V312','V313','V326','V008','V317','V3A02','V3A03','V3A04','V3A05','V3A06']
        data_info = self.data.copy()
        data_info.drop(data_info.columns.difference(in_col), 1, inplace=True)
        data_info = data_info.fillna(-999)
       
        fp_info = ['fp_info_sideff', 'fp_info_what_to_do','fp_info_other_meth','fp_info_all']
          #fp_knw =     
        for varx in fp_info:
            data_info[varx] =np.nan   
        if((table=='table7_6')|(table=='table7_5')|(table=='table5_11')):
            col_name = fp_info     
            li_temp = []     
            data_info['V326'].loc[(data_info['V326']==-999)] = np.nan
            data_info['subtr']= data_info['V008']-data_info['V317']
            for j in col_name :
                 data_info[j].loc[(data_info['V312'].isin(('1', '2','3','6','11')))&(data_info['subtr']<60)] =0
                
            data_info['fp_info_sideff'].loc[((data_info['V3A02']==1)|(data_info['V3A03']==1))&(data_info['subtr']<60)&(data_info['V312'].isin(('1', '2','3','6','11')))] =1
            data_info['fp_info_what_to_do'].loc[((data_info['V3A04']==1))&(data_info['subtr']<60)&(data_info['V312'].isin(('1', '2','3','6','11')))] =1
            data_info['fp_info_other_meth'].loc[((data_info['V3A05']==1)|(data_info['V3A06']==1))&(data_info['subtr']<60)&(data_info['V312'].isin(('1', '2','3','6','11')))] =1
            data_info['fp_info_all'].loc[(((data_info['V3A05']==1)|(data_info['V3A06']==1))&(data_info['V3A04']==1)&((data_info['V3A02']==1)|(data_info['V3A03']==1)))&(data_info['subtr']<60)&(data_info['V312'].isin(('1', '2','3','6','11')))] =1
            lv=[]
            for var_col in col_name:
                frm_temp=master_tab(data_info,'V312',var_col)
                del frm_temp[0]
                tem = frm_temp.T
                del tem[6]
                frm_temp=tem.T
                frm_temp.index =['Pill','IUD','Injectables','Implants']#list((self.meta.value_labels['V312']).values())
                frm_temp.index.name= self.meta.column_names_to_labels['V312']
                frm_temp.columns =[frm_temp.columns.name]
                if var_col == col_name[0]:
                    li_temp = frm_temp
                    continue
                li_temp = li_temp.join(frm_temp)
                p = li_temp.index.name
                li_temp.loc[p]=''
                newIndex=[p]+[ind for ind in li_temp.index if ind!=p]
                li_temp=li_temp.reindex(index=newIndex)
            lv1=li_temp
            for var_col in col_name:
                frm_temp=master_tab(data_info,'V326',var_col)
                del frm_temp[0]
                tem = frm_temp.T
                if self.year ==2011:
                    tem[10] = tem[11]+tem[12]+tem[13]+tem[14]+tem[15]
                    tem[20] = tem[21]+tem[22]+tem[23]+tem[24]+tem[25]
                    lde = [15,21,25,26,27,31,23,32,33,96]
                if self.year ==2005:
                    tem[10] = tem[11]+tem[12]+tem[13]+tem[14]+tem[15]
                    tem[20] = tem[21]+tem[22]+tem[23]+tem[24]+tem[25]
                    lde = [15,21,25,26,31,23,32,33,96]
                elif self.year ==2016: 
                    lde= [14,16,26,31,36,41,42,96]
                for d in lde:
                    k = d
                    del tem[k]
                frm_temp=tem.T
                if self.year ==2011: 
                    frm_temp.index =['Public sector','Government hospital','Government health centre','Government health station/clinic','Government health post/hew','Private medical sector','Private clinic','Pharmacy','NGO health facility']
                    frm_temp.index.name= 'Initial source of method'
                elif self.year ==2016:
                    frm_temp.index =['Government hospital','Government health station/ center','Government health post','NGO: Health facility','Private clinic','Private pharmacy']
                    frm_temp.index.name= self.meta.column_names_to_labels['V326']
                    
                frm_temp.columns =[frm_temp.columns.name]
                if var_col == col_name[0]:
                    li_temp = frm_temp
                    continue
                li_temp = li_temp.join(frm_temp) 
                p = li_temp.index.name
                li_temp.loc[p]=''
                newIndex=[p]+[ind for ind in li_temp.index if ind!=p]
                li_temp=li_temp.reindex(index=newIndex)
            lv2=li_temp
            lv = lv1.append(lv2)
            lv.columns = ['Percentage who were informed about side effects or problems of method used','Percentage who were informed about what to do if experienced side effects','Percentage who were informed by a health or family planning worker of other methods thatcould be used','Percentage who were informed of all three (Method Information Index)']   
            final_table =lv
            final_table.index.name = 'Method/source'
        else:
            return 'There is only one table for this topic!'
            
        return final_table,data_info
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def fertile_period(self, table):
        if self.year==2000:
            self.data.columns = self.data.columns.str.upper()
        # Preprocessing of data
        fe_col =  ['V013','V024','V025','V106','V502', 'V528', 'V005','V312','V217']
        data_fertile = self.data.copy()
        data_fertile.drop(data_fertile.columns.difference(fe_col), 1, inplace=True)
        data_fertile = data_fertile.fillna(-999)
        #----------------------------------------------------------------------------------
        fp_fertile = ['fp_know_fert_rhy', 'fp_know_fert_sdm']     
        for varx in fp_fertile:
            data_fertile[varx] =0   
        if((table=='table7_9')|(table=='table7_6')|(table=='table5_9')|(table=='table5_7')):
            col_name = fp_fertile  
            data_fertile['V217'].loc[(data_fertile['V217']==-999)] = np.nan
            li_temp = []     
     
            data_fertile['fp_know_fert_rhy'].loc[(data_fertile['V312']==8)] =1 
            data_fertile['fp_know_fert_sdm'].loc[(data_fertile['V312']==18)] =1
            
            for var_col in col_name:
                frm_temp=master_tab(data_fertile,var_col,'V217').T
                if var_col=='fp_know_fert_rhy':
                    del frm_temp[0]
                else:
                    pass
                if self.year ==2011:
                    frm_temp.index =frm_temp.index =['During her menstrual period','Right after her menstrual period has ended','Halfway between two menstrual periods','Just before her menstrual period begins','No specific time','Other','Don?t know','']
                
                elif self.year==2016:
                    frm_temp.index =['During her menstrual period','Right after her menstrual period has ended','Halfway between two menstrual periods','Just before her menstrual period begins','No specific time','Don?t know']
                elif self.year==2005:
                    frm_temp.index =frm_temp.index =['During her menstrual period','Right after her menstrual period has ended','Halfway between two menstrual periods','Just before her menstrual period begins','No specific time','Other','Don?t know','']
                elif self.year==2000:
                    frm_temp.index =frm_temp.index =['During her menstrual period','Right after her menstrual period has ended','Halfway between two menstrual periods','Just before her menstrual period begins','No specific time','Other','Don?t know','']
               
                    
                    
                frm_temp.columns =[frm_temp.columns.name]
                if var_col == col_name[0]:
                    li_temp = frm_temp
                    continue
                li_temp = li_temp.join(frm_temp) 
                
            final_table =li_temp
            mylist =master_tab(data_fertile,'V217')
            if ((self.year == 2011)|(self.year == 2005)|(self.year == 2000)):
                order =  [3,0,1,2,4,6,5,7]
            elif self.year == 2016:
                order =  [5,2,1,0,4,3]
                
            mylist = [mylist[i] for i in order]
            final_table['All women']=mylist
            final_table.index.name = 'Perceived fertile period'
            final_table.columns =['Users of rhythm method','Nonusers of SDM','All women']

        else:
            return 'There is only one table, table7_9, for this subtopic!'
            
        return final_table,data_fertile
#---------------------------------------------------------------------------------------------------------------------------------------------------

    def demand_need(self,table):
        if self.year==2000:
            self.data.columns = self.data.columns.str.upper()
        # Preprocessing of data
        if self.year == 2005:
            dn_col = ['V313', 'V502', 'V528', 'V005','V626','V013','V024','V025','V106','V190']
            vsix = 'V626'
        elif self.year==2000:
            dn_col = ['V313', 'V502', 'V528', 'V005','V626','V013','V024','V025','V106']
            vsix = 'V626'
            
        else:
            dn_col = ['V626A','V313', 'V502', 'V528', 'V005','V626','V013','V024','V025','V106','V190']
            vsix = 'V626A'
            
        data_demand = self.data.copy()
        data_demand.drop(data_demand.columns.difference(dn_col), 1, inplace=True)
        data_demand = data_demand.fillna(-999)
        
        fp_dem = ['Unmet need for spacing','Unmet need for limiting', 'Unmet need total', 'Met need for spacing', 'Met need for limiting', 'Met need total','Total demand for spacing','Total demand for limiting', 'Total demand - total', 'Demand satisfied by any methods', 'Demand satisfied by modern methods']
        for varx in fp_dem:
            data_demand[varx] =0   
       
        # Need and demand for family planning among currently married and All women women according to background characteristics
        col_name = fp_dem
        if self.year==2000:
                bcar = ['V013','V025','V024','V106']
        else:        
            bcar = ['V013','V025','V024','V106','V190' ]
        li_temp = []
        lo =[]
        for var_bc in bcar:
            data_demand['Unmet need for spacing'].loc[(data_demand[vsix]==1)] = 1
            data_demand['Unmet need for limiting'].loc[(data_demand[vsix]==2)] = 1
            data_demand['Unmet need total'].loc[((data_demand[vsix]==2)|(data_demand[vsix]==1))] = 1
                
            data_demand['Met need for spacing'].loc[(data_demand[vsix]==3)] = 1
            data_demand['Met need for limiting'].loc[(data_demand[vsix]==4)] = 1
            data_demand['Met need total'].loc[((data_demand[vsix]==3)|(data_demand[vsix]==4))] = 1
                
            data_demand['Total demand for spacing'].loc[(data_demand[vsix]==1)|(data_demand[vsix]==3)] = 1
            data_demand['Total demand for limiting'].loc[(data_demand[vsix]==2)|(data_demand[vsix]==4)] = 1
                
            data_demand['Total demand - total'].loc[(data_demand[vsix].isin(('1', '3','2','4')))] =1
                
            data_demand['Demand satisfied by modern methods'].loc[((data_demand[vsix]==3)|(data_demand[vsix]==4))&(data_demand['V313']==3)] = 1
            data_demand['Demand satisfied by modern methods'].loc[(data_demand[vsix].isin(('0', '7','8','9')))] =np.nan
                
            data_demand['Demand satisfied by any methods'].loc[(data_demand[vsix]==3)|(data_demand[vsix]==4)] = 1
            data_demand['Demand satisfied by any methods'].loc[(data_demand[vsix].isin(('0', '7','8','9')))] =np.nan
            
            if((table=='table7_10_1')|(table=='table7_7')|(table=='table7_3')|(table=='table7_5')): 
                for m in fp_dem:
                    data_demand[m].loc[(data_demand['V502']!=1)] = np.nan
     
                    
            for var_col in col_name:
                
                frm_temp=master_tab(data_demand,var_bc,var_col)
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
        
        if table=='table7_10_2':
            q = final_table.index.name
            final_table.loc[q]=''
            newIndex=[q]+[ind for ind in final_table.index if ind!=q]
            final_table=final_table.reindex(index=newIndex)
            final_table= final_table.rename(index={'Background characterstics':'All Women'})
            

        return final_table,data_demand
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def decision_making(self, table):
        # Preprocessing of data
        if self.year==2000:
            self.data.columns = self.data.columns.str.upper()
            
        if (self.year==2011)|(self.year==2005)|(self.year==2000):
            dm_col = ['V502', 'V528', 'V005','V632','V213','V312','V013','V024','V025','V106','V190','V219']
        elif (self.year==2016):
            dm_col = ['V632A', 'V502', 'V528', 'V005','V632','V213','V312','V013','V024','V025','V106','V190','V219']
        data_decision = self.data.copy()
        data_decision.drop(data_decision.columns.difference(dm_col), 1, inplace=True)
        data_decision = data_decision.fillna(-999)
        #----------------------------------------------------------------------------------
        if (self.year==2011)|(self.year==2005)|(self.year==2000):
            fp_demak = ['Currently using FP:Mainly wife','Currently using FP:Wife and husband jointly', 'Currently using FP:Mainly husband']
       
        elif (self.year==2016):
            fp_demak = ['Currently using FP:Mainly wife','Currently using FP:Wife and husband jointly', 'Currently using FP:Mainly husband','Currently using FP:Other','Currently not using FP:Mainly wife','Currently not using FP:Wife and husband jointly', 'Currently not using FP:Mainly husband','Currently not using FP:Other' ]
       
        for varx in fp_demak:
            data_decision[varx] =0
            
        def my_recode(row):
            
            if row == 0: return '0'
            elif (row==1)|(row==2): return '1-2'
            elif (row==3)|(row==4): return '3-4'
            elif row>=5: return '5+'
            
        data_decision['Number of living children'] = data_decision['V219'].apply(my_recode)
        if (table =='table7_11')|(table=='table5_dec')|(table=='table7_dec'):
            
            # Need and demand for family planning among currently married and All women women according to background characteristics
            col_name = fp_demak
            if self.year==2000:
                bcar = ['V013','Number of living children','V025','V024','V106']
            else:
                bcar = ['V013','Number of living children','V025','V024','V106','V190' ]
            li_temp = []
            lo =[]
            for var_bc in bcar:
                data_decision['Currently using FP:Mainly wife'].loc[(data_decision['V632']==1)] = 1
                data_decision['Currently using FP:Wife and husband jointly'].loc[(data_decision['V632']==2)] = 1
                data_decision['Currently using FP:Mainly husband'].loc[(data_decision['V632']==3)] = 1
                if self.year ==2016:
                    data_decision['Currently using FP:Other'].loc[(data_decision['V632']==6)] = 1
                    data_decision['Currently not using FP:Mainly wife'].loc[(data_decision['V632A']==1)] = 1
                    data_decision['Currently not using FP:Wife and husband jointly'].loc[(data_decision['V632A']==2)] = 1
                    data_decision['Currently not using FP:Mainly husband'].loc[(data_decision['V632A']==3)] = 1
                    data_decision['Currently not using FP:Other'].loc[(data_decision['V632A']==6)] = 1
                    
                for demk in range(len(fp_demak)):
                    if demk<=3:
                        data_decision[fp_demak[demk]].loc[(data_decision['V502']!=1)|(data_decision['V213']!=0)|(data_decision['V312']==0)] =np.nan
                    else:
                        data_decision[fp_demak[demk]].loc[(data_decision['V502']!=1)|(data_decision['V213']!=0)|(data_decision['V312']!=0)] =np.nan
                              
     
                   
                for var_col in col_name:
                    frm_temp=master_tab(data_decision,var_bc,var_col)
                    if self.year ==2000:
                        if var_bc =='Number of living children':
                            pass
                        else:
                            var_bc= var_bc.lower()
                            if ((var_bc =='v013')|(var_bc =='v025')|(var_bc =='v024')|(var_bc =='v106')):
                                frm_temp.index =list((self.meta.value_labels[var_bc]).values())
                                frm_temp.index.name= self.meta.column_names_to_labels[var_bc]
                                var_bc= var_bc.upper()
                    else:        
                        if ((var_bc =='V013')|(var_bc =='V025')|(var_bc =='V024')|(var_bc =='V106')|(var_bc =='V190')):
                            frm_temp.index =list((self.meta.value_labels[var_bc]).values())
                            frm_temp.index.name= self.meta.column_names_to_labels[var_bc]
                            
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
            if self.year==2000:
                final_table =((((lo[0].append(lo[1])).append(lo[2])).append(lo[3])).append(lo[4]))
            else:    
                final_table =((((lo[0].append(lo[1])).append(lo[2])).append(lo[3])).append(lo[4])).append(lo[5])
            final_table.index.name = 'Background characterstics'
        else:
            return 'There is only one table, table7_11, for this subtopic!'
            
        
        return final_table,data_decision
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def future_use_contra(self, table):
        if self.year==2000:
            self.data.columns = self.data.columns.str.upper()
        # Preprocessing of data
        fu_col = ['V502', 'V005','V312','V013','V024','V025','V106','V190','V362','V219']
        data_future = self.data.copy()
        data_future.drop(data_future.columns.difference(fu_col), 1, inplace=True)
        data_future = data_future.fillna(-999)
        #----------------------------------------------------------------------------------
        fp_future = ['Intends to use','Unsure', 'Does not intend to use']
        li_temp = []
        total =[]
        for varx in fp_future:
            data_future[varx] =0
            
        def my_recode(row):
            
            if row == 0: return '0'
            elif (row==1): return '1'
            elif (row==2): return '2'
            elif (row==3): return '3'
            elif row>=4: return '4+'
            
        data_future['Number of living children'] = data_future['V219'].apply(my_recode)
        if((table=='table7_12')|(table=='table7_8')|(table=='table5_14')|(table=='table5_15')): 
            
            col_name = fp_future
            bcar = ['Number of living children']
          
            data_future['Intends to use'].loc[(data_future['V362']==2)] = 1
            data_future['Unsure'].loc[(data_future['V362']==4)] = 1
            data_future['Does not intend to use'].loc[(data_future['V362']==5)] = 1
            for f in fp_future:
                data_future[f].loc[(data_future['V502']!=1)|(data_future['V312']!=0)] =np.nan
                
            total =[master_tab(data_future,col_name[0])[1] ,master_tab(data_future,col_name[1])[1],master_tab(data_future,col_name[2])[0]]
            for var_col in col_name: 
                frm_temp=master_tab(data_future,'Number of living children',var_col) 
        
                del frm_temp[0]
                frm_temp.columns =[frm_temp.columns.name]
                if var_col == col_name[0]:
                    li_temp = frm_temp
                    continue
                li_temp = li_temp.join(frm_temp)
                                             
            final_table =li_temp.T
            final_table.index.name = 'Intention to use in the future'
            final_table['Total'] = total
        else:
            return 'There are only three  table, table7_12, table7_8 and table5_14, for this subtopic!'
        
        return final_table,data_future
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def exposure_message(self, table):
        # Preprocessing of data
        if self.year==2000:
            self.data.columns = self.data.columns.str.upper()
            
        ex_col = ['V384A','V384B','V384C','V384D','S815D','S815E','S815G','S714D','S714E','V632', 'V502', 'V005','V013','V024','V025','V106','V190']
        data_exposure = self.data.copy()
        data_exposure.drop(data_exposure.columns.difference(ex_col), 1, inplace=True)
        data_exposure = data_exposure.fillna(-999)
        #----------------------------------------------------------------------------------
        if self.year == 2011:
            fp_exp = ['Radio','Television', 'News paper/magazine','Pamphlet/posters/leaflets','Community event/conversation','None of these six media soruces']
        elif self.year==2016:
            fp_exp = ['Radio','Television', 'News paper/magazine','Pamphlet/posters/leaflets','Community event/conversation','Internet', 'Mobile phone message','None of these six media soruces']
        elif self.year==2005:
            fp_exp = ['Radio','Television', 'News paper/magazine','None of these three media soruces']
      
            
        for varx in fp_exp:
            data_exposure[varx] =0   
       
        if((table=='table7_13')|(table=='table7_9')|(table=='table5_17')):
            col_name = fp_exp
            bcar = ['V013','V025','V024','V106','V190' ]
            li_temp = []
            lo =[]
            for var_bc in bcar:
                data_exposure['Radio'].loc[(data_exposure['V384A']==1)] = 1
                data_exposure['Television'].loc[(data_exposure['V384B']==1)] = 1
                data_exposure['News paper/magazine'].loc[(data_exposure['V384C']==1)]=1
                if self.year ==2016:
                    data_exposure['Mobile phone message'].loc[(data_exposure['V384D']==1)] = 1
                    data_exposure['Pamphlet/posters/leaflets'].loc[(data_exposure['S815D']==1)] = 1
                    data_exposure['Community event/conversation'].loc[(data_exposure['S815E']==1)] = 1
                    data_exposure['Internet'].loc[(data_exposure['S815G']==1)] = 1
                    data_exposure['None of these six media soruces'].loc[(data_exposure['V384A']==0)&(data_exposure['V384B']==0)&(data_exposure['V384C']==0)&(data_exposure['V384D']==0)&(data_exposure['S815D']==0)&(data_exposure['S815E']==0)&(data_exposure['S815G']==0)] =1
                
                elif self.year == 2011:
                    data_exposure['Pamphlet/posters/leaflets'].loc[(data_exposure['S714D']==1)] = 1
                    data_exposure['Community event/conversation'].loc[(data_exposure['S714E']==1)] = 1
                    data_exposure['None of these six media soruces'].loc[(data_exposure['V384A']==0)&(data_exposure['V384B']==0)&(data_exposure['V384C']==0)&(data_exposure['S714D']==0)&(data_exposure['S714E']==0)] =1
                elif self.year ==2005:
                    data_exposure['None of these three media soruces'].loc[(data_exposure['V384A']==0)&(data_exposure['V384B']==0)&(data_exposure['V384C']==0)] =1
          
                    
                    
                    
                for var_col in col_name:
                    frm_temp=master_tab(data_exposure,var_bc,var_col)
                    frm_temp.index =list((self.meta.value_labels[var_bc]).values())
                    frm_temp.index.name= self.meta.column_names_to_labels[var_bc]
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
            
            final_table =(((lo[0].append(lo[1])).append(lo[2])).append(lo[3])).append(lo[4])
            final_table.index.name = 'Background characterstics'
        else:
            return 'There are only three  table, table7_13, table7_9 and table5_17, for this subtopic!'   

        return final_table,data_exposure
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def contact_provider(self, table):
        if self.year==2000:
            self.data.columns = self.data.columns.str.upper()
        # Preprocessing of data
        con_col = ['V393','V394','V395','V502', 'V312', 'V005','V013','V024','V025','V106','V190']
        data_contact = self.data.copy()
        data_contact.drop(data_contact.columns.difference(con_col), 1, inplace=True)
        data_contact = data_contact.fillna(-999)
        fp_exp = ['fp_fpvisit_discuss','fp_hf_discuss','fp_hf_notdiscuss','fp_any_notdiscuss']
        for varx in fp_exp:
            data_contact[varx] =0   
       
        if((table=='table7_14')|(table=='table7_11')|(table=='table5_18')|(table=='table5_20')):
            col_name = fp_exp
            if self.year==2000:
                bcar = ['V013','V025','V024','V106']
            else:
                bcar = ['V013','V025','V024','V106','V190' ]
            li_temp = []
            lo =[]
            for var_bc in bcar:
                data_contact['fp_fpvisit_discuss'].loc[(data_contact['V393']==1)] = 1
                data_contact['fp_hf_discuss'].loc[(data_contact['V394']==1)&(data_contact['V395']==1)] = 1
                data_contact['fp_hf_notdiscuss'].loc[(data_contact['V394']==1)&(data_contact['V395']!=1)] = 1
                data_contact['fp_any_notdiscuss'].loc[(data_contact['V393']!=1)&(data_contact['V395']!=1)] = 1
                for var in col_name:
                    data_contact[var].loc[(data_contact['V312']!=0)] =np.nan
                 
                   
                for var_col in col_name:
                   
                    frm_temp=master_tab(data_contact,var_bc,var_col)
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
            fil_col=['Women non-users that were visited by a FP worker who discussed FP','Women non-users who visited a health facility in last 12 months and discussed FP','Women non-users who visited a health facility in last 12 months and did not discuss FP','Women non-users who did not discuss FP neither with FP worker or in a health facility']
            final_table.columns = fil_col
        else:
            return 'There are only three  table, table7_14, table7_11 and table5_18, for this subtopic!'   

        return final_table,data_contact


