# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:19:08 2023

@author: hp
"""

#Libraries can be installed (using PiP) and then imported.
#We used PIP to install pandas but JSON file comes pre packaged in anaconda.

#Installing Matplotlib for plots and charts in python using pip in cmd prompt
#Syntax: pip install matplotlib 

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Method to read JSON data
json_file = open('loan_data_json.json') #opens the JSON file
data = json.load(json_file) #this loads the JSON data in to panda.'.load' function exists in the python library for json

# transform to a dataframe
loandata = pd.DataFrame(data)

loandata.info()

#finding unique values in the data column
loandata['purpose'].unique()

#describe the data 
loandata.describe()

#describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#Using exponent function for log of annual income
income = np.exp(loandata['log.annual.inc'])

loandata['annualincome'] = income

#Fico score

fico = 700

# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    ficocat = 'Good'
elif fico >=700: 
    ficocat = 'Excellent'
else:
    ficocat  = 'Unknown'
print(ficocat)


#Iterators For_Loop: Apply the above fico categories to every value or row of the fico score.
#Note if we type the following syntax in the console, it will give us the number of rows. 
# dataframe['columnname']

length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category < 600:
        cat = 'Poor'
    elif category >= 601 and category < 660:
        cat = 'Fair'
    elif category >= 660 and category < 700:
        cat = 'Good'
    elif category >=700: 
        cat = 'Excellent'
    else:
        cat  = 'Unknown'
    print(cat)
    ficocat.append(cat)
    
#Now putting the cat column in the dataframe

ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat

# df.loc as Conditional statement: Can make a new column with a condition
# Syntax: df.loc(df(columnname) condition, NewColumnName) = If condition is met

#For interest rates, a new column is wanted. Rate > 0.12 then high else low

loandata.info()

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type']= 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type']= 'Low'

#MatplotLib: Number of loans by fico category

catplot = loandata.groupby(['fico.category']).size() 
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar()
plt.show()

# Scatter Plots

loandata.info()

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()

#writing to CSV
loandata.to_csv('Loan_cleaned.csv',index = True)


















