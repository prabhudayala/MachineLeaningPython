# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 22:37:20 2018

@author: prabhudayala
"""
import matplotlib.pyplot as plt
import pandas as pd
alldata=pd.read_csv("ign.csv")
#print(alldata.head())
#print(alldata.tail())
print(alldata.shape)
#print(alldata.iloc[:5,:2])
alldata=alldata.iloc[:,1:]
#print(alldata.shape)
#print(alldata.loc[:5,:])
#print(alldata.index)
#print(alldata.loc[:5,["score_phrase","score"]])
#print(alldata["score_phrase"])
#print(alldata[["score_phrase","score"]])
#print(type(alldata["score_phrase"]))
s1=pd.Series([1,2,3,4,5,6,7,8,9,10])
#print(s1)
s2=pd.Series([2,3,4,5,6,7,8,9,10,11])
df=pd.DataFrame(
    [
        [1,2],
        ["Boris Yeltsin", "Mikhail Gorbachev"]
    ],
    index=["row1", "row2"],
    columns=["column1", "column2"]
)
#print(df)
#print(df.loc[:,:])
df=pd.DataFrame(
    {
        "column1":[1,2],
        "column2":["Boris Yeltsin", "Mikhail Gorbachev"]
        
    }
)
#print(df)
#print(alldata["score"].mean())
#print(alldata.mean())
#print(alldata.mean(axis=1))
#print(alldata.corr())
#print(alldata["score"]/2)
x=alldata["score"] > 7
#print(x)
y=alldata[x]
#print(y)
x=(alldata["score"] > 7) & (alldata["platform"] == "Xbox One")
y=alldata[x]
#print(y)
#alldata[alldata["platform"] == "Xbox One"]["score"].plot(kind="hist")
#plt.show()
#alldata[alldata["platform"] == "PlayStation 4"]["score"].plot(kind="hist")
#plt.show()
alldata["score"].plot(kind="hist")