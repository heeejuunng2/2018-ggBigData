import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

wifiCsv_path="freewifi.csv"
free_wifi=pd.read_csv(wifiCsv_path, encoding='euc-kr')
# print(free_wifi.head())

free_wifi=free_wifi[['설치장소명','와이파이SSID','소재지도로명주소','관리기관전화번호']]
# print(free_wifi.head())
free_wifi.rename(columns={free_wifi.columns[0]:'설치장소',
                          free_wifi.columns[2]:'도로명주소',
                          free_wifi.columns[3]: '전화'},inplace=True)
print(free_wifi.head())
print("-"*100)

print("중복")
print(free_wifi['와이파이SSID'].unique())
print(free_wifi['전화'].unique())
#중복된거 하나만 나옴
print("-"*100)

for i in range(0,37):
    free_wifi=free_wifi.rename(index={i:(str(i+1))})
print(free_wifi.head())
print("-"*100)

# print(free_wifi.ix[7])

#시각화 => 수치 형태 데이터가 아니라서 실패 ㅠㅠ


