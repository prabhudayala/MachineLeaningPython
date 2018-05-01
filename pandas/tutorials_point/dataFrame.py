# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 22:01:29 2018

@author: prabhudayala
"""

import pandas as pd
import numpy as np

#pandas.DataFrame( data, index, columns, dtype, copy)
df=pd.DataFrame()
print(df)

#dataframe from list
data=[[1,2,3,4],[5,6,7,8]]
df=pd.DataFrame(data)
#print(df)


data=[[1,'Alice'],[2,'Bob'],[3,'Camel']]
df=pd.DataFrame(data)
#print(df)


data=[[1,'Alice'],[2,'Bob'],[3,'Camel']]
df=pd.DataFrame(data,columns=['Seriel number','Name'])
df=pd.DataFrame(data,columns=['Seriel number','Name'],dtype=float)
#print(df)



#Create a DataFrame from Dict of ndarrays / Lists
data={'Name':['alice','bob','caren','david'],'title':['a','b','c','d']}
df=pd.DataFrame(data)
df=pd.DataFrame(data,index=[1,2,3,4])
#print(df)



#Create a DataFrame from List of Dicts
data=[{'a':'alice','b':'bob'},{'a':'axe'}]
df=pd.DataFrame(data)
df=pd.DataFrame(data,index=[1,2])
#print(df)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
#print(df1)
#print(df2)



#reate a DataFrame from Dict of Series
data={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d',])}
df=pd.DataFrame(data)
#print(df)
#print(df)



#column addition
data={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d',])}
df=pd.DataFrame(data)
df['three']=pd.Series([10,20,30],index=['a','b','c'])
#print(df)
df['four']=df['three']+df['one']
#print(df)



#column deletion
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
     'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(d)
#print (df)

# using del function
del df['one']
#print (df)
df.pop('two')
#print (df)



#Row Selection, Addition, and Deletion
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
#print (df.loc['b'])
#print (df.iloc[2])
#print (df.iloc[1:3])



#Addition and deletion of rows
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
print( df)

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df = df.append(df2)
df = df.drop(0)
print (df)