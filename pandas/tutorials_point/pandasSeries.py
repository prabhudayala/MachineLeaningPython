# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 22:01:29 2018

@author: prabhudayala
"""

import pandas as pd
import numpy as np
s = pd.Series()
print (s)

#series from np array
data=np.array(['a','b','c','d'])
#print(data)
#pandas.Series( data, index, dtype, copy)
s=pd.Series(data)
#print(s)

s=pd.Series(data,index=[100,101,102,103])
#print(s)




#series from dictionary
data={'a':1,'b':2,'c':3,'d':4}
#print(data)
#pandas.Series( data, index, dtype, copy)
s=pd.Series(data)
#print(s)

s=pd.Series(data,index=['a','b','c','d','e'])
#print(s)


#Create a Series from Scalar
s= pd.Series(5)
#print(s)

s= pd.Series(5,index=[1,2,3,4,5,6])
#print(s)



#Accessing Data from Series with Position
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[0])
#Retrieve Data Using Label (Index)
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[['a','b','c']])