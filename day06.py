# 데이터프레임(DataFrame) : 데이터가 담겨있는 표(데이터 표)
# 결측치(누락값) 처리?

import pandas as pd
# pandas 모듈을 pd라는 이름으로 가져와라
from pandas import DataFrame
# pandas 모듈에 있는 DataFrame메서드를 가져와라
# import 묘듈 -> pandas : 모듈
# from 모듈 import 메서드 -> DataFrame : 메서드

# 패키지, 모듈, 메서드?
# 패키지: 모듈의 묶음 -> BigData 패키지
# 모듈 : py확장자를 갖는 파일(파이선 파일) -> day06 이런거..
# 메서드 : 모듈의 여러개의 메서드로 구성

df_left=DataFrame({'KEY':['K0','K1','K2','K3'],
           'A': ['A0', 'A1', 'A2', 'A3'],
           'B': [0.5, 2.2, 3.6, 0.4]})

df_right=DataFrame({'KEY':['K2','K3','K4','K5'],
           'C': ['C2', 'C3', 'C4', 'C5'],
           'D': ['D2', 'D3', 'D4', 'D5']})
print(df_left)
print(df_right)
#여러개의 데이터프레임 합치기
# df_all=pd.merge(df_left,df_right)
# print(df_all)
# KEY값이 공통이므로 , KEY를 기준으로 합침
# KEY값중 겹치는게 K2,K3이므로 K2,K3가 들어가는 거끼리 합쳐짐

df_all=pd.merge(df_left,df_right,how='outer')
# 중복 없앰, 값 없는거 까지 합침, 값없는건 NaN으로 표시
print(df_all)
print("="*50)
print(pd.isnull(df_all))
# 값이 널인지 아닌지 조사, 값이 없으면 True, 값이 있으면 False
print("$"*50)
print(df_all.isnull())
# 위에랑 결과 같음, 둘다됨
print("@"*50)
print(pd.notnull(df_all))
# 값이 없으면 False, 값이 있으면 True
print("*"*50)
print(df_all.notnull())
print("&"*50)
print(df_all)

# 데이터프레임 참조방법 : DataFrame.ix[[첫번째행, 두번째행],[첫번째열, 두번째열]]
#                        ex) df_all.ix[[첫번째행, 두번째행],[첫번째열, 두번째열]]
print(df_all.ix[[0,1], ['A','B']])

print(df_all)
print("%"*50)
print(df_all.isnull().sum()) #" 열 "마다, null이 몇개있는지 출력
print(df_all['A'].isnull().sum()) # A열의 null이 몇개가 있는가
print(df_all.notnull().sum()) #null이 아닌것들의 개수 출력

print(df_all)
print(df_all.isnull().sum()) # 열단위 null 개수
print(df_all.isnull().sum(1)) #행단위 null 개수
df_all['Nan_Cnt']=df_all.isnull().sum(1)
# 새로운 열 추가 : 열제목 = 추가할 열의 데이터
# 행단위 null 개수 추가
print("="*50)
print(df_all)
print("*"*50)
df_all['Notnull_Cnt']=df_all.notnull().sum(1)
# 행단위 null이 아닌개수 출력
print(df_all)