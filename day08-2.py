import urllib.request #외부에서 url 가져오는 모듈(패키지)
import pandas as pd
from pandas import DataFrame
import numpy as np

suicide_rate_url="http://apps.who.int/gho/athena/data/xmart.csv?t" \
             "arget=GHO/MH_12&profile=crosstable&filter=COUNTRY:*;RE" \
             "GION:*&x-sideaxis=COUNTRY&x-topaxis=GHO;YEAR;SEX"
local_filename, headers =\
    urllib.request.urlretrieve(suicide_rate_url, filename="who_suicide_rates.csv")
                      #retrieve :검색하다
# print("[local_filename]:" , local_filename)
# print("[headers]:", headers)

path_csv="who_suicide_rates.csv"
df_rates=pd.read_csv(path_csv, skiprows=2) #skiprows=2 :2행 건너뛰고 출력
print(df_rates.head())
print('-'*100)

df_rates=df_rates[['Country',' Both sexes',' Male',' Female']] #2015년 데이터
print(df_rates)
print('-'*100)
df_rates.columns=['Country','Both','Male','Female']
print(df_rates)
print('-'*100)

#시각화
import matplotlib.pyplot as plt
# df_rates.plot.hist() #Male, Female, Both가 출력됨
# df_rates.plot.hist(y=['Male','Female']) #Male, Female 출력됨
# df_rates.plot.hist(y=['Male','Female'], bins=30)
#Male, Female 출력됨, 구간을 30개로 나눔
# df_rates.plot.hist(y=['Male','Female'], bins=30, color=['Coral','Yellow'])
# plt.xlabel("Suicide number")
# plt.ylabel("Number of Countries")
# plt.title("Number of Suicide By Countries")
# plt.legend()
# plt.show()

#Male 데이터, Female데이터의 평균 구하기
print(df_rates['Male'].mean(), df_rates['Female'].mean())
df_rates.boxplot(['Both','Male','Female'])
plt.xlabel("Suicide number")
plt.ylabel("Number of Countries")
plt.title("Number of Suicide By Countries")
plt.show()

# 1) 데이터수집: open api,인터넷,스크래핑(BeautifulSoup),크롤링((Selenium),DB)
# 2) 데이터전처리(정제, 결측치 처리, 제거, 잡음(이상치,outlier)제거 등)
# 3) 데이터변환(처리하기에 용이한 형태로)
# 4) 데이터분석(통계적 방법)
# 5) 시각화(막대, 원형, 박스 등)
# 6) 예측/분류(머신러닝, 딥러닝)
# 7) 모델 평가 및 개선