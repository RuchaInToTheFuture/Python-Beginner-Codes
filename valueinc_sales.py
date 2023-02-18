# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:48:47 2023

@author: hp
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <==== format

data = pd.read_csv('transaction.csv')

# A CSV (comma-separated values) saves a workbook as a comma delimited text file.
# But the given data file has semicolon separating columns.
# Next step is separating the data columns grouped into one column.

data = pd.read_csv('transaction.csv',sep=';')

# Summary of the data 

data.info()

#Working with Calculations
#Defining variables for a specific transaction

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6 

#Mathematical Operations 

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = ProfitPerItem * NumberOfItemsPurchased

SalesPerTransaction = SellingPricePerItem * NumberOfItemsPurchased

CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# CostPerTransaction Column calculation
# CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#To single out and bring out a column: variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# Adding CostPerTransaction as a column in the dataframe.

data['CostPerTransaction'] = CostPerTransaction

# Adding SalesPerTransaction 

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Adding Profit = Sales - Cost 

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# MarkUp = (Sales - Cost)/Cost

data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

#Rounding the markup column

data['Markup'] = round(data['Markup'],2)

# Combining data fields: combine day,month,date
#Using Concatonating strings

my_date = 'Day' + '-' + 'Month' + '-' + 'Year'

#The above data type looks good but we cannot concatonate strings and integers. 

#checking data type

data.info()

type('Day')

#Change data type of column
# Python has a function called S-Type to change the the data type.

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day + '-' + data['Month'] +'-' + year

#Please note that day and year are variables but month is a whole column that was already an object.

# We are adding the column to our data.

data['my_date'] = my_date

#Using iloc to view specific columns/rows. 
# iloc is part of pandas library that spilts your data into subsets.

data.iloc[0] #views the row with the index = 0 
data.iloc[0:3] #First 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #First 5 rows

data.iloc[:,2] #All your rows but 2 columns

data.iloc[4,2] #Brings in 4th row, 2nd column

# Using split to split client keywords column
#new_var = column.str.split('Separator', expand =True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#Creating three new columns for split_col 

data['ClientAge']= split_col[0]

data['ClientType']= split_col[1]

data['LengthOfContract']= split_col[2]

#Getting rid of square brackets in col 0 and 2.
#Using the replace function similar to excel function

data['ClientAge'] = data['ClientAge'].str.replace('[','')

data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')

#Using the lower function to change item to lower case

data['ItemDescription'] = data['ItemDescription'].str.lower()

#Joining Data: Merging two files 
#Bringing in a new data set

seasons = pd.read_csv('value_inc_seasons.csv', sep = ';')

#merge_dataframe = pd.merge(dataframe_old,dataframe_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

# Eliminating unnecessary columns
# dataframe = dataframe.drop('columnname',axis = 1)

data = data.drop('ClientKeywords', axis = 1)

data = data.drop('Day', axis = 1) 

#Dropping multiple columns: use a list!

data = data.drop(['Year','Month'], axis = 1)

#Export into a CSV
# Dataframe has an index column. If you want to include it we say 'true' otherwise 'False')


