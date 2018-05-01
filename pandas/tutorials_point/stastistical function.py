# -*- coding: utf-8 -*-
"""
Created on Tue May  1 13:21:49 2018

@author: prabhudayala
"""

import pandas as pd
import numpy as np
s = pd.Series([1,2,3,4,5,4])
print (s.pct_change())

df = pd.DataFrame(np.random.randn(5, 2))
print (df.pct_change())
sx = pd.Series(np.random.np.random.randn(5), index=list('abcde'))

sx['d'] = sx['b'] # so there's a tie

#rank method for tie braeaking
print (sx.rank(method='max'))