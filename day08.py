# 리스트, 시리즈
# 리스트: 데이터들이 값으로만 구성
# 시리즈: 데이터들이 값+인덱스로 구성, 인덱스를 지정하지 않으면 0,1,2,3 ,, 자동생성
from pandas import Series, DataFrame
import numpy as np
sp_list=[10,20,30,40,50]
print(sp_list)
sp_series=Series([11,22,33,44,55]) #값에 인덱스까지
print(sp_series)

print(sp_list[3])
print(sp_series[3])

print("-"*50)

sp_series_withindex=Series([11,22,33,44,55],
                           index=['a','b','c','d','e'])
print(sp_series_withindex)
print(sp_series_withindex[1]) #1번째 위치
print(sp_series_withindex['b']) #'b' 행번호 접근
print("-"*50)

sp_list=[10,20,30,40,50]
sp_series=Series([11,22,33,44,55],
                index=['a','b','c','d','e'])
print(sp_series)
print(sp_series.index) #->인덱스만 출력
print(sp_series.values) #->값만 출력
print("-"*50)

for i in sp_series.index: #여기서 i는 'a','b','c'..를 읽어옴
    print("index:"+i+"    value:"+str(sp_series_withindex[i]))
print("-"*50)

print('c' in sp_series) #sp_series안에 'c'가 들어가 있나요? -> True
print("-"*50)

print(sp_series*100) #각각의 요소에 x100 씩 됨
print("-"*50)

print(sp_series.values)
print(sp_series.values>30)
print(sp_series[sp_series.values>30]) #false를 만나면 출력X
#30보다 큰값들만 sp_series에 참조해서 출력
print(sp_series[sp_series>30]) #code 43번줄 = code 45번줄
print("-"*50)

# print(sp_series.name) #None 출력
sp_series.name='☆뿅뿅뿅☆'
# print(sp_series.name)
print(sp_series)
print(sp_series.index)
print(sp_series.values)
print(sp_series.shape)
print("size:"+str(sp_series.size))
print("ndim(차원):"+str(sp_series.ndim))
print("-"*50)

print(sp_series['c']) #c행의 값
# print(sp_series['a','c']) #error
print(sp_series[['a','c']]) #a행과 c행의 값(행이름 포함)
#Q . 그냥 11, 33만 출력하려면 ?
print("-"*50)

print(sp_series.count())
print(len(sp_series))
print("-"*50)

#인덱스(행)로 찾을때
print(sp_series.at['a'])
print(sp_series.iat[0])
print(sp_series.iat[2])
# print(sp_series.ix[0]) #경고
# print(sp_series.ix['b']) #경고
print(sp_series.loc['b'])
print("-"*50)

search_index=[0,3]
sp_list=[10,20,30,40,50]
print([i+2 for i in search_index])  #search_index에서 값을 읽어서 i에 넣어라
     #대괄호로 묶여있으므로 리스트 #그리고 그 i를 출력해라
print([sp_list[i] for i in search_index])
print('-'*50)

#dict(딕션어리) 생성 = {'키' : 값}
sdic={'Ohio':1000, "Texas":2000, "Oregon":3000}
print(sdic)
print(type(sdic))
print('-'*50)

#dictionary -> series로 변경을 원함
srs3=Series(sdic)
print(srs3)
print('-'*50)

states=['California','Ohio','Oregon']
srs4=Series(sdic, index=states) #california는 없으므로 Nan
print(srs4)
print('-'*50)
print(srs4.isnull())
print(srs4.notnull())
print('-'*50)