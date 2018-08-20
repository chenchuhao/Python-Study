# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 15:28:07 2018

@author: chenchuhao

"""

import pandas as pd
import numpy as np
from pandas  import Series
from pandas import DataFrame 
from numpy.random import randn
import random

df = DataFrame({'key1':['a','a','b','b','a'],
                'key2':['one','two','one','two','one'],
                'data1':randn(5),
                'data2':randn(5)})

people = DataFrame(randn(5,5),
                   columns = ['a','b','c','d','e'],
                   index = ['Joe','steve','Wes','Jim','Travis'])
people.ix[2:3,['b','c']]=np.nan
mapping = {'a':'red','b':'red','c':'blue','d':'blue','e':'red','f':'reange'}
by_column = people.groupby(mapping,axis = 1)
by_column.sum()
map_series = Series(mapping)
people.groupby(map_series,axis=1).count()

people.groupby(len).sum()

key_list = ['one','one','one','two','two']

people.groupby([len,key_list]).min()

columns = pd.MultiIndex.from_arrays([['US','US','US','JP','JP'],[1,3,5,1,3]],names = ['cty','tenor'])
hier_df = DataFrame(randn(4,5),columns = columns)
hier_df.groupby(level = 'cty',axis = 1).count()


#数据聚合
grouped = df.groupby('key1')
grouped['data1'].quantile(0.9)

def peak_to_peak(arr):
    return arr.max()-arr.min()
grouped.agg(peak_to_peak)


#添加”消费占总额百分比“的列
tips = pd.read_csv(r'E:\pydata-book\examples\tips.csv')
tips['tip_pct'] = tips['tip']/tips['total_bill']
def f(sex):
    if random.randint(0,1000)<500:
        return 'Female'
    else :
        return 'Male'
tips['sex']=''
tips['sex']=tips['sex'].apply(f)

grouped = tips.groupby(['sex','smoker'])
grouped_pct = grouped['tip_pct']
grouped_pct.agg('mean')    
grouped_pct.agg(['mean','std',peak_to_peak])
#grouped_pct.agg([('foo','bar'),('bar',np.std)])
functions = ['count','mean','max']
result = grouped['tip_pct','total_bill'].agg(functions)
#不同列应用不同函数
grouped.agg({'tip':np.max,'size':sum})
tips.groupby(['sex','smoker'],as_index=False).mean()

#分组级运算和转换  transform 和apply
k1_mean = df.groupby('key1').mean().add_prefix('mean_')
df.merge(k1_mean,left_on='key1',right_index=True)

key = ['one','two','one','two','one']
people.groupby(key).mean()
people.groupby(key).transform(np.mean)
#各组减去平均值
def deman(arr):
    return arr-arr.mean()
demaned = people.groupby(key).transform(deman)

result = tips.groupby('smoker',group_keys=False)['tip_pct'].describe()

#透视表和交叉表
#透视表pivot_table
tips.pivot_table(index=['sex','smoker'])
tips.pivot_table(['tip_pct','size'],index = ['sex','day'],columns = 'smoker')
tips.pivot_table(['tip_pct','size'],index = ['sex','day'],columns = 'smoker',
                 margins = True)
tips.pivot_table('tip_pct',index = ['sex','smoker'],columns = 'day',
                 aggfunc = len,margins = True)
tips.pivot_table('size',index = ['time','sex','smoker'],columns = 'day',
                 aggfunc = sum,margins = True,fill_value = 0)

#交叉表crosstab
pd.crosstab([tips.time,tips.day],tips.smoker,margins = True)


#2012年联邦选举委员会数据库
fec = pd.read_csv(r'E:\pydata-book\datasets\fec\P00000001-ALL.csv')
parties = {'Bachmann, Michelle': 'Republican',  
                  'Cain, Herman': 'Republican',  
                  'Gingrich, Newt': 'Republican',  
                  'Huntsman, Jon': 'Republican',  
                  'Johnson, Gary Earl': 'Republican',  
                  'McCotter, Thaddeus G': 'Republican',  
                  'Obama, Barack': 'Democrat',  
                  'Paul, Ron': 'Republican',  
                  'Pawlenty, Timothy': 'Republican',  
                  'Perry, Rick': 'Republican',  
                  "Roemer, Charles E. 'Buddy' III": 'Republican',  
                  'Romney, Mitt': 'Republican',  
                  'Santorum, Rick': 'Republican',  
           }  
fec['party'] = fec.cand_nm.map(parties)
fec = fec[fec.contb_receipt_amt>0]
fec_mrbo = fec[fec.cand_nm.isin(['Romney, Mitt','Obama, Barack'])]
#根据职业和雇主统计赞助信息  
occ_mapping = {  
        'INFORMATION REQUESTED PER BEST EFFORTS': 'NOT PROVIDED',  
        'INFORMATION REQUESTED': 'NOT PROVIDED',  
        'INFORMATION REQUESTED (BEST EFFORTS)': 'NOT PROVIDED',  
        'C.E.O.': 'CEO'  
        } 
#如果未提供相关映射，则返回x  
f = lambda x : occ_mapping.get(x,x)
fec.contbr_occupation = fec.contbr_occupation.map(f)
#同样处理雇主信息  
emp_mapping = {  
        'INFORMATION REQUESTED PER BEST EFFORTS': 'NOT PROVIDED',  
        'INFORMATION REQUESTED': 'NOT PROVIDED',  
        'SELF': 'self-EMPLOYED',  
        'SELF EMPLOYED': 'self-EMPLOYED',  
}  
#如果未提供相关映射，则返回x 
f = lambda x: emp_mapping.get(x,x)
fec.contbr_employer = fec.contbr_employer.map(f)
#根据党派和职业进行聚合，并过滤出总出资金额不足200万的数据
by_occupation = fec.pivot_table('contb_receipt_amt',
                                columns = 'party',
                                index = 'contbr_occupation',
                                aggfunc = np.sum)
over_2mm = by_occupation[by_occupation.sum(1)>2000000]

#对Obabam和Romney总出资最高的的职业和企业  
def get_top_amounts(group, key, n=5):  
    totals = group.groupby(key)['contb_receipt_amt'].sum().sort_values(ascending=False)  
    #根据key对totals进行将序排列  
    return totals[:n]
#根据职业和雇主进行聚合  
grouped = fec_mrbo.groupby('cand_nm')  
#print (grouped.apply(get_top_amounts, 'contbr_occupation', n=7))  
#print (grouped.apply(get_top_amounts, 'contbr_employer', n=10))

#对出资额进行分组
bins = np.array([0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
lables = pd.cut(fec_mrbo.contb_receipt_amt,bins)
#根据姓名和元标签进行分组
grouped = fec_mrbo.groupby(['cand_nm',lables])
grouped.size()
bucket_sums = grouped.contb_receipt_amt.sum().unstack(0)
normed_sums = bucket_sums.div(bucket_sums.sum(axis=1), axis=0)
normed_sums[:-2].plot(kind = 'barh',stacked=True)




