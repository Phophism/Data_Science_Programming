# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 14:45:26 2021

Title Quiz 6
@author: akkapop 640631128
"""
import pandas as pd

#import csv
df = pd.read_csv('Salaries.csv',header=0,index_col = False , names = None)

""" Try to read the first 10, 20, 50 records """
df.head() # first 5 rows
df.head(10) # first 5 rows
df.head(20) # first 5 rows
df.head(50) # first 5 rows

""" How to view the last few records """
df.tail() # last 5 rows

""" 1-2 """
# group by
df_rank = df.groupby(['rank'])
df_rank = df_rank.mean()
df_rank

""" 3 """
# group by then average salary
df_rank = df.groupby('rank')[['salary']].mean()
df_rank

""" 4 """
# group by then sort (for potential speedup)
df.groupby(['rank'], sort = False)[['salary']].mean()

""" 5-6 """
# Filtering
df_sub = df[ df['salary'] > 120000 ] # select df where salary in df greater than 120000
df_sub
df_f = df[ df['sex'] == 'Female' ] # select df where sex is female
df_f

""" 7 """
# slicing
# select salary col
df['salary']

""" 8 """
# select rank and salary 
df[['rank', 'salary']]

""" 9 """
# select rows by their position 
df[10:20] # row 11 to row 20

""" 10 """
# loc # select using labels
df_sub.loc[10:20,['rank','sex','salary']] # select rank,sex,salary from df where salary > 120000 # row 11 to row 20

""" 11 """
# iloc # select using index
df_sub.iloc[10:20,[0,3,4,5]] # select the selected column(index 0,3,4,5) from df # row 11 to 20 

""" 12 """
# sort
df_sorted = df.sort_values(by = 'service') # sort by service
df_sorted.head()

""" 13 """
# sort 2
df_sort = df.sort_values(by=['service','salary'],ascending=[True,False]) # sort by service asc , then salary desc
df_sort.head(10)
