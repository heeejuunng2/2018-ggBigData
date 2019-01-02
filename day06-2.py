import pandas as pd
import numpy as np #행열 연산에 도움을 줌
from pandas import DataFrame

print(np.arange(10))
print(np.arange(10).shape)

#1차원 -> 2차원(5행 2열)으로 재정의
df=print(np.arange(10).reshape(5,2))
print(type(df)) #2차원 배열타입
df=DataFrame(np.arange(10).reshape(5,2),
             index=['a','b','c','d','e'],
             columns=['C1','C2'])
# index=[ 행이름] , columns= [열이름]
# print(type(df)) #DataFrame타입
print(df)

# Quiz) b행 C1열 값을 None값으로 변경
# 값을 강제로 None값으로 만들기
# df_all.ix [[행],[열]] =None
# df.ix[['b'], ['C1']]=None
df.ix[['b','e'], ['C1']]=None
# b,c행 C2열의 값(2)을 None으로 변경
df.ix[['b','c'], ['C2']]=None
print("*"*50)
print(df)

print(df.sum()) #None은 0으로 처리, 각 열의 합
print(df['C1'].sum()) #C1열의 합
print(df['C1'].cumsum()) #C1열에 해당하는 누적합
print("*"*50)
#Quiz
df_grade=DataFrame({'KOR' : [70,80,90,90,45],
                    'ENG' : [60,40,80,95,43],
                    'MAT' : [90,50,87,90,40]},
                   index=['KIM','LEE','PARK','CHOI','CHO'])
print(df_grade)








