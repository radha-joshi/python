#pandas in python

#Radha Joshi [122-A]
import pandas as pd
import numpy as np

ser=pd. Series ()
print("pandas series" ,ser)

data=np.array(['a','b','c','d'])
ser=pd.Series(data)
print("pandas series: \n", ser)

#Radha Joshi [122-A]
info={
"2014": [100.5, 150.6, 200.9, 3000, 5000],
"2015": [1200, 1800, 2200, 5000, 6000],
"2016": [2000, 4000,5000, 7000, 8000],
"2017": [4000, 6500, 5500, 8000, 10000],
}
names=["ankit", "nazneen", "sumit", "akshada", "shruti"]
df=pd.DataFrame(info, index=names)
print (df)

#Radha Joshi [122-A]
#sales for the year 2015
print("\nSales in 2015")
print(df["2015"])

#sales made by sumit across all years
print("\nSumit's Sales")
print(df.loc["sumit"])

#total amount of sales for every single year
print("\nTotal Sales Per Year")
print(df.sum())

#Radha Joshi [122-A]
#summary of the whole table
print("\nSummary Statistics")
print(df.describe())
