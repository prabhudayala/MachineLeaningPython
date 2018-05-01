# -*- coding: utf-8 -*-
"""
Created on Tue May  1 10:27:44 2018

@author: prabhudayala
"""
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

#select all rows for a specific column
#print (df.loc[['b','g'],['A','D']])
#print (df.loc[['b','g'],:])
#print (df.loc['a':'f'])
#print (df.loc['a']>0)
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print (df[1:1])