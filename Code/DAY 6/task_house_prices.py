import csv
import numpy as np
import pandas as pd
house_data = pd.read_csv("house_price.csv")
house_data.head()
def Task5():
  print("Mean is " + str(house_data.mean()[0]))
  print("Variance is " + str(house_data.var()[0]))
  print("SD is " + str(house_data.std()[0]))
  print("Median is " + str(house_data.median()[0]))
  print("25th Percentile is " + str(house_data.quantile(.25)[0]))
  print("50th Percentile is " + str(house_data.quantile(.50)[0]))
  print("99th Percentile is " + str(house_data.quantile(.99)[0]))
  per_99 = house_data.quantile(.99)[0]
  above_99 = []
  for i in house_data["House_Size"]:
    if(i > per_99):
      above_99.append(i)
  print("Values that exceed the 99th percentile are",end = " ")
  for i in above_99:
    print(i,end=' ')

Task5()

# Output

# Mean is 2003.6363636363637
# Variance is 2117186.147186147
# SD is 1455.055375986133
# Median is 1475.0
# 25th Percentile is 1125.0
# 50th Percentile is 1475.0
# 99th Percentile is 6474.999999999997
# Values that exceed the 99th percentile are 7000 
