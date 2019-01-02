import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

subwayCsv_path="subway.csv"
subwayCsv=pd.read_csv(subwayCsv_path, encoding='euc-kr')
# print(subwayCsv.head())
print('-'*50)

subwayCsv.rename(columns={subwayCsv.columns[2]:'하루평균'},inplace=True)
# print(subwayCsv.head())

subwayCsv.index.name='구분'
print(subwayCsv.head())
print("-"*100)

for i in range(0,5):
    subwayCsv=subwayCsv.rename(index={i:str(i+1)+')'})
print(subwayCsv.head())
print("-"*100)

# print(olive_oil['id_area'][0].split('.')[0])
for i in range(0,5):
    print(subwayCsv['하루평균'][i].split(',')[0])
print('-'*100)

#시각화
subwayCsv.plot.hist(bins=100,color='blue')
plt.xlabel("Mean of the day")
plt.ylabel("Rank")
plt.title("Ues Subway")
plt.legend()
plt.show()










