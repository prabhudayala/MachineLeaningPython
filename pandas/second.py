# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 22:01:29 2018

@author: prabhudayala
"""

import pandas as pd
import math

import numpy as np

def clean_income(value):
    if value == "$200,000 and up":
        return 200000
    elif value == "Prefer not to answer":
        return np.nan
    elif isinstance(value, float) and math.isnan(value):
        return np.nan
    value = value.replace(",", "").replace("$", "")
    income_high, income_low = value.split(" to ")
    return (int(income_high) + int(income_low)) / 2

def genderDecider(x):
    if isinstance(x,float) and math.isnan(x):
        return x
    else:
        return int(x=="Female")
    

data = pd.read_csv("thanksgiving-2015-poll-data.csv", encoding="Latin-1")
#print(data.head())
#print(data["Do you celebrate Thanksgiving?"].unique())
#print(data.columns[64:])
#print(data["What is your gender?"].value_counts(dropna=False))
data["gender"]=data["What is your gender?"].apply(genderDecider)
#print(data["gender"].value_counts(dropna=False))
#data.apply(lambda x:print(x.dtype)).head()
#print(data["How much total combined money did all members of your HOUSEHOLD earn last year?"].value_counts(dropna=False))
data["income"]=data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(clean_income)
#print(data["income"].head())
#print(data["What type of cranberry saucedo you typically have?"].value_counts())
homemade=data[data["What type of cranberry saucedo you typically have?"]=="Homemade"]
canned=data[data["What type of cranberry saucedo you typically have?"]=="Canned"]
grouped=data.groupby("What type of cranberry saucedo you typically have?")
#for name, group in grouped:
#    print(name)
#    print(group.shape)
#    print(type(group))
#print(grouped["gender"].head())
#print(grouped["income"].agg(np.mean))
sauce = grouped.agg(np.mean)
#sauce["income"].plot(kind="bar")
grouped = data.groupby(["What type of cranberry saucedo you typically have?", "What is typically the main dish at your Thanksgiving dinner?"])
#print(grouped.agg(np.mean))
#x=grouped.agg([np.mean,np.sum,np.std])
#x["income"]["mean"].plot(kind="bar")
grouped=data.groupby("How would you describe where you live?")
x=grouped.agg("count")
x["income"].plot(kind="bar")
#grouped.apply(lambda x : print(x.value_counts()))