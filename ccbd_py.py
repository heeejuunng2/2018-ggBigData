import os
import sys
import pandas as pd
from pandas import DataFrame
import numpy as np

# csv_path="ccbd.csv"
ccbd_data=pd.read_csv("ccbd.csv",encoding='euc-kr')
print(ccbd_data)
print("="*50)
print(ccbd_data.head(3))
#앞에서 3개 읽어오기
print(ccbd_data.tail(3))
#뒤에서 3개 읽어오기

print("="*50)
print(ccbd_data['금 년(6.21~6.30)'])
#저 제목에 해당하는 데이터 나옴
print("="*50)
ccbd_data.rename(columns={ccbd_data.columns[1] : "금년6"},
                 inplace=True)
#ccbd_data의 1번째 열이름을 금년6으로 바꿈
print(ccbd_data)
print(type(ccbd_data))
print("*"*50)

df=DataFrame([1000,2000,3000,4000])
print(df)

df=DataFrame([1000,2000,3000,4000],index=['i1','i2','i3','i4'])
print(df)

df=DataFrame({'C1':[1000,2000,3000,4000]},index=['i1','i2','i3','i4'])
print(df)

print("-"*50+"{[1]}")

df2=DataFrame({'c1': [1,2,3],
               'c2': [11,22,33],
               'c3': [111,222,333]})
print(df2)

df2=DataFrame({'c1': [1,2,3],
               'c2': [11,22,33],
               'c3': [111,222,333]},
              index=['i1','i2','i3'])
print(df2)
print("-"*50+"{[2]}")

df3=DataFrame(columns=('lib','qt1','qt2'))
print(df3)

for i in range(5):
    df3.loc[i]=[(i+1)*(n+1) for n in range(3)]
print(df3)
print("-"*50+"{[3]}")

df4=DataFrame(np.random.randn(6,3))
# 평균0, 표준편차1인 6행3열 난수 발생
print(df4)

lst1=[1,2,3,4]
print(lst1)
df=DataFrame(lst1)
# 리스트를 데이터 프레임에 담으면 데이터프레임처럼변함
print(df)

lst2=[[1,2,3,4,5],['a','b','c','d','e']]
# 열 : 맨 안쪽에 있는 대가로의 원소의 개수 ->5열
# 행 : 대가로로 묶여있는 개수 -> 2행
df=DataFrame(lst2)
print(df)
print("="*50)

#사전식으로 데이터 프레임 생성
data={
    'name' : ['a','b','c'],
    'year' : [2018,2019,2020]
}
print(type(data))

df=DataFrame(data,index=['eb','it','mi'])
print(df)
print(type(df))

df=DataFrame([10,20,30,40])
df2=DataFrame({'x1':[1,2,3],
                'x2':[11,22,33],
                'x3':[111,222,333]})
df3=DataFrame({'c1':[1,2,3],
                'c2':[11,22,33],
                'c3':[111,222,333]},
              index=['i1','i2','i3'])
print(df)
print(df2)
print(df3)


df.columns=['군포'] #df 열 이름 주기
print(df)
df2.columns=['z1','z2','z3']
print(df2)

#이름바꾸기
df2.rename(columns={'z2':'마징가z', 'z3':'태권v'}
            ,inplace=True)
print(df2)

print(df)
df.columns.values[0]=999
#열중에 0번째열의 내용을 999로 바꿔라
print(df)

print(df3)
df3.columns.values[1]='국어'
print(df3)

print(df)
df['newC2']=5
print(df)

df['newC3']=['a','b','c','d']
print(df)

print(df2)
df2['new9']=df2['태권v']>300
print(df2)

df2['new9']=df2['마징가z']+df2['태권v']
print(df2)

# Quiz) df2에 new10열 추가(z1, 마징가z, 태권v값의 평균)
df2['new10']=(df2['z1']+df2['마징가z']+df2['태권v'])/df2.__len__()
print(df2)
print("*"*50)

df9=DataFrame([10,20,30,40], index=['i1','i2','i3','i4'])
print(df9)
print("="*50)
from pandas import Series
addsrs=Series([11,21,31,41], index=['i1','i2','i3','i4'])
print(addsrs)
print(type(addsrs))

#df9에 addsrs 추가
df9['c4']=addsrs
print(df9)

addsrs2=Series([11,21,31], index=['i3','i4','i5'])
df9['c4']=addsrs2
print(df9)
print("*"*50)

df22=DataFrame() #빈 데이터프레임
df22.append({'c1':'', 'c2':'', 'c3':''},ignore_index=True)
print(df22)

df33=DataFrame(columns=('c1','c2','c3'))
print(df33)
print("="*50)

df2=DataFrame({'c1': [1,2,3],
               'c2': [11,22,33],
               'c3': [111,222,333]})
df2=DataFrame({'c1': [1,2,3],
               'c2': [11,22,33],
               'c3': [111,222,333]},
              index=['i1','i2','i3'])
print(df2)
del df2['c2'] #c2열 삭제
print(df2)
df2=df2.drop('c1',1) #(제거하고자 하는열, 1)
print(df2)

print(df3)
df3=df3.drop(['c2','c3'],1)
print(df3)
print("="*50)

# Quiz
print("Quiz01---------------------------------------")
# df11=DataFrame({'name': ['kim','lee','park'],
#                 'age': [17,16,18],
#                 'addr': ['gunpo','seoul','incheon'],
#                 'sname': ['gildong','soonsin','chul']},
#                index=['student1','student2','student3'])
# print(df11)
data={'name':['kim','lee','park'],
      'age': [17,16,18],
      'addr': ['gunpo','seoul','incheon'],
      'sname':['gildong','soonsin','chul']}
mydf=DataFrame(data,index=['student1','student2','student3'])
print(mydf)

print("Quiz02---------------------------------------")
mydf2=mydf['age'].max()
print(mydf2)

print("Quiz03---------------------------------------")
import matplotlib.pyplot as plt
mydf3=mydf[['name','age']]
mydf3.plot.hist()
plt.show()




