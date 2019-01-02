import pandas as pd
from pandas import DataFrame

df=DataFrame([10,20,30,40], index=['i1','i2','i3','i4'])
print(df)

df=DataFrame({'c1':[10,20,30,40],
              'c2':[11,21,31,41],
              'c3':[12,22,32,42]},
             index=['i1','i2','i3','i4'])
print(df)

print(df['c2']) #c2열에 있는 데이터 출력
print(df[['c2']]) #c2열에 있는 데이터 및 열의 이름까지 출력
print(df[['c1','c3']]) #c1,c3열에 있는 데이터 및 열의 이름까지 출력

# 행 이름으로 데이터 참조
print("="*50)
print(df)
print("="*50)
print(df.ix[0,0]) #10
print("="*50)
print(df.ix[1:3 , 0:2]) #1~2까지 행, 0~1까지 열의 "교차"지점 값 참조
#참고 ) Deprecation Warning은 무시..
# 빅데이터 과학자(분석가)
# ->파이썬/R 코딩 , 통계, 수학(방정식,행렬...미적분) 필요
print("="*50)

# .iloc : 정수로 위치를 지정해서 값을 참조하는 방식
# .loc : label을 가지고 값을 참조
# .ix : 정수 및 label모두 사용 가능
import numpy as np
s=pd.Series(np.nan, index=[49,48,47,46,45,1,2,3,4,5])
#데이터 표라고 보면됨, 표에 nan을 집어넣어라
print(s)
print("====<.iloc>"+"="*50)
print(s.iloc[:3]) #인덱스가 0~2까지
print("====<.loc>"+"="*50)
print(s.loc[:3]) #3이라는 레이블(행)이 나올때 까지
print("====<.ix : 숫자>"+"="*50)
print(s.ix[:3])
#3이 숫자이면 레이블(행) 기반 참조로 하기 때문에, s.loc[:3]결과와 같음
print("====<.ix : 문자+숫자>"+"="*50)
s2=pd.Series(np.nan, index=['a','b','c','d','e',1,2,3,4,5])
print(s2.ix[:6])
#레이블이 숫자와 문자로 구성된 경우에는 0~5번째까지 참조

print("="*50)
df=DataFrame({'c1':[10,20,30],
              'c2':[11,21,31],
              'c3':[12,22,32]},
             index=['i1','i2','i3'])
print(df)
print("="*50)

print(df[['c2']]) #c2열 출력
print("="*50)

df['c3']=df['c1']+df['c2']
# c3 의 값을 c1+c2값으로 바꾸기
print(df)
print("="*50)

df['c3']=111 #값 하나주면 전부 111로 치환됨
print(df)
print("="*50)

df['newC4']=['a','b','c']
print(df)
print("="*50)

print(df.ix[2,2]) #111
print("="*50)

df.ix[1,2]=2000 #1,2자리를 2000으로 바꾸기
print(df)
print("="*50)

print(df)
rows=[4,44,444,'d'] #행추가
# print(len(df))
# print(df.loc[1])
df.loc[len(df)]=rows
df=df.rename(index={3:'i4'}) #새로운 행이름(3)을 i4로 이름바꿈
print(df)
print("="*50)

df2=DataFrame()
#열단위로 데이터 추가
df2=df2.append({'c1':'','c2':'','c3':''}, ignore_index=True)
print(df2)
print("="*50)
df2.ix[0, 'c1']='111'
# 0번째행 c1열에 데이터 111을 넣어라
df2.ix[0, 'c2']='222'
df2.ix[0, 'c3']='333'
print(df2)
print("="*50)

df3=DataFrame(columns=('c1','c2','c3')) #열이름 주기
print(df3)
df3.loc[0]=['111','222','333'] #0행에 데이터 추가
print("="*50)
print(df3)
print("="*50)
print(df)
print("-------i2행,c2열 삭제--------")
df=df.drop('i2',axis=0) #axis=0 이면 i2행을 제거하라는 의미
df=df.drop('c2',axis=1) #axis=1 ,'c2'이면 c2열을 제거하라는 의미
print(df)
print("="*50)
print(df.T) #Transpose 행,열 변화시킴 : 전치행렬
print("="*50)
print(df.values) #값만 출력(array형태로)
print("="*50)
print(df.shape) #3행3열 출력

print("="*50)
df=DataFrame({'c1':[10,20,30],
              'c2':[11,21,31],
              'c3':[12,22,32]},
             index=['i1','i2','i3'])
print(df)
print()
df=df.reindex(['i1','i2','i3','i4','i5'])
print(df)

print("="*50)
df=df.reindex(['i1','i2','i3','i4','i5']).interpolate()
#inerpolate() 를 지정해주면 NaN 자리에 가장 마지막 자리의 값으로 다 채워짐
print(df)

print("="*50)
df['interPo']=df['c1'].interpolate()
print(df)

print("="*50)
#중복일 경우
df=df.reindex(['i1','i2','i4','i4','i5'])
print(df)
print("="*50)
print(df.index.is_unique) #is_unique :인덱스가 유일하냐 ?
# i4중복이라 아니므로 False 나옴
print("="*50)
print(df.ix['i4'])

print("="*50)
df7=DataFrame({'c1':[10,20,30],
              'c2':[11,21,31],
              'c3':[12,22,32]},
             index=['i1','i2','i3'])
df7.index.name='id_area9' #인덱스의 이름을 줌(행이름 주기)
print(df7)

print("==<정렬하기>"+"="*40)
df=DataFrame({'c2':[10,40,70],
              'c3':[50,20,20],
              'c1':[60,30,90]},
             index=['i2','i1','i3'])
print(df)
print("<1>"+"="*50)
print(df.sort_index()) #인덱스를 기준으로 정렬
print("<2>"+"="*50)
print(df.sort_index(axis=0)) #행기준
print("<3>"+"="*50)
print(df.sort_index(axis=1)) #열기준
print("<4>"+"="*50)
print(df)
print(df.sort_index(axis=0,ascending=False))
#인덱스를 기준으로 내림차순정렬 ascending=True면 오름차순
print("<5>"+"="*50)
print(df)
print(df.sort_values(by='c1')) #c1을 기준으로 정렬해라
print(df.sort_values(by='c1', ascending=False))
print(df.sort_values(by=['c3','c2'])) #c3기준 다음 c2기준 정렬

print("="*50)
# NULL 처리(NaN, NA, NULL)
from numpy import nan as NA #np.nan을 NA로 사용하게 만듬
df=DataFrame(np.random.randn(7,3)) # .randn : 난수 정규분포
print(df)
print("="*50)
df.loc[2,1]=NA
df.loc[3,2]=NA
print(df)
print("="*50)

df.replace(NA, 'NULL VALUE', inplace=True)
# NA -> NULL VALUE
print(df)
print("="*50)

#딕션어리 이용한 데이터 프레임
data={
    'name':['c','b','a','e','d'],
    'year':[2020,2018,2019,2017,2020],
    'reports':[4,24,31,2,3],
    'coverage':[25,94,57,62,70] } #5행 4열
# 참고) coverage : 범위, 보도 media coverage : 미디어 보도
df=DataFrame(data, index=['jtbc','sbs','kbs','mbc','ytn'])
print(df)
print("="*50)
df=df.rank(axis=0) #행단위 랭크 , 오름차순
print(df)
# print("="*50)
# df=df.rank(axis=1)
# print(df)
































