# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 16:13:51 2021

Data Science Programming
Title : HW6 : Avocado
@author: akkapop prasompon 640631128

"""
import pandas as pd

filepath = "D:\\Akkapop\\Data_Science\\1st_year\\semester_1\\DS_pro\\Assignment\\Data_Science_Programming\\avocado\\HW6\\avocado.csv"
data = pd.read_csv(filepath,index_col=0) #ignore index
data

""" 1.1) Which region sold the largest amount of avocado ? """
sold_by_country = data.groupby(['region'],as_index=False)[['Total Volume']].sum().sort_values('Total Volume', ascending = False) # group by region, don't remove region, sum value in each region, order by sum desc
sold_by_country.head() ## Determine top 5 records

#         region  Total Volume
#51       TotalUS  5.864740e+09
#52          West  1.086779e+09
#6     California  1.028982e+09
#45  SouthCentral  1.011280e+09
#29     Northeast  7.132809e+08

# we ignore total amount (totalus).
sold_by_countries = sold_by_country[1:] # remove first row which is TotalUS
sold_by_countries # display result

most_sold = sold_by_countries.iloc[[0]] # select the new first row
most_sold_region = most_sold.iloc[0,0] # select first cell (region)
most_sold_region
# Answer 1.1
# West is the region that sold the largest amount of avocado 

""" 1.2)  In this region, where the biggest lot of sold avocado came from (4046, 4225, 4770) ? """
msr_data = data[ data['region'] == most_sold_region ] # most_sold_region_data , select only data that contain 'west'
msr_data # display result

# display the result of 'west' data
# sort by 4046 4225 4770 in desc order so the largest value will be on the top
# show only select column
msr_data.sort_values(['4046','4225','4770'] , ascending = False).iloc[[0],3:6] 
# Answer 1.2
# as the result : the biggest lot of sold avocado came from (4046, 4225, 4770) in 'west'
#        4046        4225       4770
#  4377537.67  2558039.85  193764.89

""" 2.1) Which region sold the smallest amount of avocado ? """

# without using min(), change desc for 1.1 and 1.2 to asc

sold_by_country_asc = data.groupby(['region'],as_index=False)[['Total Volume']].sum().sort_values('Total Volume', ascending = True) # group by region, don't remove region, sum value in each region, order by sum desc
sold_by_country_asc.head() ## Determine top 5 records

#        region  Total Volume
#49    Syracuse   10942667.68
#3        Boise   14413187.75
#47     Spokane   15565275.48
#0       Albany   16067799.97
#23  Louisville   16097002.40

less_sold = sold_by_country_asc.iloc[[0]] # select the new first row
less_sold
less_sold_region = less_sold.iloc[0,0] # select first cell (region)
less_sold_region
# Answer 2.1
# Syracuse is the region that sold the smallest amount of avocado 

""" 2.2) In this region, where the biggest lot of sold avocado came from (4046, 4225, 4770) ? """
# same method like 2.2)

lsr_data = data[ data['region'] == less_sold_region ] # less_sold_region_data , select only data that contain 'Syracuse'
lsr_data # display result

lsr_data.sort_values(['4046','4225','4770'] , ascending = False).iloc[[0],3:6] 
# Answer 2.2
# as the result : the biggest lot of sold avocado came from (4046, 4225, 4770) in 'Syracuse'
#      4046      4225   4770
#  10004.38  57087.01  102.7

""" 3) Which region sold the highest price of avocado in average ? """

avg_price_region = data.groupby('region',as_index=False)[['AveragePrice']].mean() # find mean of average price of each region
max_avg_price = avg_price_region[['AveragePrice']].max()[0] # find max average price
max_avg_price_region = avg_price_region[ avg_price_region['AveragePrice'] == max_avg_price ] # find region with max average price
max_avg_price_region.iloc[0,0] # Display region with highest average price
# Answer 3.
# 'HartfordSpringfield' is the region that sold the highest price of avocado in average

""" 4) Find the total amount of income (Avg_Price*Total_Volume) of each region. """

data_income = data.groupby(['region'],as_index=False).agg(TotalVol=('Total Volume','sum'),AveragePrice=('AveragePrice','mean')) # Group by region generate 2 columns contains sum of total volumn and average of average avocado price
data_income['income'] =  data_income['TotalVol']*data_income['AveragePrice'] # add income column 
data_income # Answer 4.

""" 
5) Let AVOCADO  Average Weight : 4046 => 4 ounces, 4225 => 9 ounces, 4770 => 12 ounces
    5.1) Find the number of sold avocadoes by region ?
"""

# create new data frame groupby region and contains total amount of each avocado type
data_oz = data.groupby(['region'],as_index=False).agg(sum_4046=('4046','sum'),
                                                      sum_4225=('4225','sum'),
                                                      sum_4770=('4770','sum')
                                                      )

# create new columns conatain total weight in oz. of each type
data_oz['4046_oz'] = data_oz['sum_4046']*4
data_oz['4225_oz'] = data_oz['sum_4225']*9
data_oz['4770_oz'] = data_oz['sum_4770']*12

data_oz['total_oz'] = data_oz.iloc[:, 4:7].sum(axis=1) # create new column contains total amount of avocado (oz) in each region
data_oz = data_oz[data_oz.region != 'TotalUS'] # ignore TotalUS
data_oz.loc[:, ['region','total_oz']].sort_values('total_oz', ascending=False) # Answer 5.1 : Display number of sold avocadoes by region 

""" 5.2) Which region sold the largest number of avocados ? """

max_oz = data_oz[['total_oz']].max()[0] # find the largest number of avocado
data_oz[ data_oz['total_oz'] == max_oz ].iloc[0,0] # Display region(index=0) that contains largest number of avocado
# Answer 5.2
# California is the region that sold the largest number of avocados 

""" 6) Normally, the customers buy the avocados by unit or in a bags ? """

data_prop = data[data['region'] != 'TotalUS'] # I don't want total amount to be calculated. So, I drop TotalUS from dataframe 

# To compare the proportion between amount of avocado by unit and bag
# According to central limit theorem, I don't have to use groupby()
# Since, I just find the average of total unit and total bag then compare the proportion

sum_4046 = data_prop['4046'].sum()
sum_4225 = data_prop['4225'].sum()
sum_4770 = data_prop['4770'].sum()
total_unit = sum_4046+sum_4225+sum_4770 # total avocado by unit --- (1)
total_bag = data_prop['Total Bags'].sum()  # total avocado by bag --- (2)
total_avocado = data_prop['Total Volume'].sum()  # total avocado --- (3)

proportion_unit = total_unit/total_avocado # find the proportion of unit and total volume --- (1)/(3)
proportion_bag = total_bag/total_avocado  # find the proportion of unit and total bag --- (2)/(3)

# display the result
proportion_unit # = 0.717
proportion_bag # = 0.283

# Answer 6. : (short answer : unit)
# As the result we can notice that amount of sold avocado in unit is higher than bag
# We can assume that customers prefer to buy the avocado by unit

"""  
Optional

7) Which month is the best time to sell avocado

8)  Baseon the data in 2015, is it true that the region which higher population can sell more avocados?

"""