import csv
import numpy as np
import pandas as pd
data = pd.read_csv("agilitix_ocr_data.csv")
def Task_1(m1,m2):
  breaker = 0
  for i in data["Month"]:
    if i == m1:
      breaker = 1
      print(data.loc[data['Month'] == i]["Mumbai"].values[0])
    elif breaker==1:
      print(data.loc[data['Month'] == i]["Mumbai"].values[0])
      if i == m2:
        breaker = 0
Task_1("Jul-11","Sep-11")

#      Month  Hyderabad  Delhi   Mumbai
# 18  Jul-11      449.0  540.0  1030.88
#      Month  Hyderabad   Delhi   Mumbai
# 19  Aug-11      539.0  532.09  1102.42
#      Month  Hyderabad   Delhi  Mumbai
# 20  Sep-11     539.89  569.99  1208.2

# Output
# 1030.88
# 1102.42
# 1208.2
