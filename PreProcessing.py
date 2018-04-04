import math
import numpy as np
import csv
import collections
import pandas as pd
df1=pd.read_csv("train_sample.csv")
# print(df1['click_time'])
time=df1['click_time']
t=[]
date=[]
ttime=[]
for item in time:
    date.append(int(item[9]))
    per=(int(item[11])*10)+int(item[12])
    ttime.append(per)



df1['date']=date
df1['time']=ttime


del df1['click_time']
del df1['attributed_time']
df1.to_csv('cleaned_train.csv')