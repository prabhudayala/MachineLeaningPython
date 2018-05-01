# -*- coding: utf-8 -*-
"""
Created on Tue May  1 10:27:44 2018

@author: prabhudayala
"""

import pandas as pd
import numpy as np
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s)
#print ("Split Pattern:")
#print (s.str.split(' '))
#print (s.str.get_dummies())
print (s.str.repeat(3))

with pd.option_context("display.max_rows",10):
   print(pd.get_option("display.max_rows"))
   print(pd.get_option("display.max_rows"))