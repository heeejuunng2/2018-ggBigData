import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import nltk.corpus
import requests
from bs4 import BeautifulSoup

# 1. 문자열 인덱싱
# 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.
pin = "881120-1068234"
print(pin[7:8])
print("-"*50)

# 2. 문자열 변경
# 다음과 같은 문자열이 있다.
# 1980M1120
# 위 문자열을 다음과 같이 변경하시오.
# M19801120
str="1980M1120"
print('M'+str.split('M')[0]+str.split('M')[1])
print("-"*50)

# 3. 문자열 바꾸기1
# 다음과 같은 문자열이 있다.
# a:b:c:d
# 문자열의 replace 함수를 이용하여 위 문자열을 다음과 같이 고치시오.
# a#b#c#d
str="a:b:c:d"
str=str.replace(":","#")
print(str)
print("-"*50)

# 4. 리스트 삭제
# [1, 2, 3, 4, 5]라는 리스트를 [1, 3, 5]로 만들어 보자.
list=[1,2,3,4,5]
list.remove(2)
list.remove(4)
print(list)
print("-"*50)

# 5. dict함수 사용
# 딕셔너리 a에서 'B'에 해당되는 값을 추출하고 삭제해 보자.
a = {'A':90, 'B':80, 'C':70}
print(a['B'])
del a['B']
print(a)
print("-"*50)

# 6. 조건문
# 홍길동씨의 행운권 번호는 23번 이라고 한다. 다음은 행운권 당첨번호 리스트이다.
lucky_list = [1, 9, 23, 46]
# 홍길동씨가 당첨되었다면 “야호”라는 문자열을 출력하는 프로그램을 작성하시오.
if 23 in lucky_list:
    print('야호')
print("-"*50)

# 7. 50점 이상의 총합
# 다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상의 점수들의 총합을 구하시오.
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum=0
for i in A:
    if i>=50:
        sum+=i
print(sum)
print("-"*50)

# 8. 별 표시하기
# while문을 이용하여 아래와 같이 별(*)을 표시하는 프로그램을 작성해 보자.
# *
# **
# ***
# ****
i=1
while i<5:
    print("*"*i)
    i+=1
print("-" * 50)

# 9.혈액형
# 다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다.
data=['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
# for 문을 이용하여 각 혈액형 별 학생수의 합계를 구하시오.
suma=sumb=sumab=sumo=0
for i in data:
    if i=='A':
        suma+=1
    if i=='B':
        sumb+=1
    if i=='AB':
        sumab+=1
    if i=='O':
        sumo+=1
answer="A형 : "+str(suma)+" B형 : "+str(sumb)+" AB형 : "+str(sumab)+" O형 : "+str(sumo)
print(answer)


print("-" * 50)

# 10. 5의 배수의 총합
# for문을 이용하여 1부터 1000까지의 자연수 중 5의 배수에 해당되는 자연수들의 총합을 구하시오.
for i in range(1,1001):
    if i%5==0:
        sum+=i
print(sum)
print("-" * 50)

# 1) 데이터수집: open api,인터넷,스크래핑(BeautifulSoup),크롤링((Selenium),DB)
# 2) 데이터전처리(정제, 결측치 처리, 제거, 잡음(이상치,outlier)제거 등)
# 3) 데이터변환(처리하기에 용이한 형태로)
# 4) 데이터분석(통계적 방법)
# 5) 시각화(막대, 원형, 박스 등)
# 6) 예측/분류(머신러닝, 딥러닝)
# 7) 모델 평가 및 개선

# 11. 임의의 웹사이트로부터 데이터 추출-> 전처리 -> 시각화
delivery_path="woman safe delivery.csv"
woman_delivery=pd.read_csv(delivery_path, encoding='euc-kr')
# print(woman_delivery.head())
woman_delivery=woman_delivery[['명칭','택배함 수','이용건수(2016-08)','이용건수(2017-08)']]
woman_delivery.rename(columns={woman_delivery.
                           columns[0]:'설치장소'},inplace=True)
woman_delivery.index.name='구분'

print(woman_delivery)

fig, ax= plt.subplots()
ax.barh(woman_delivery['택배함 수'],woman_delivery['이용건수(2017-08)'],
        color='Coral')
ax.set_xlabel('Number Of Ues')
ax.set_ylabel('Number Of Boxes Shipped')
ax.set_title("A woman's safe delivery service")
plt.grid(True)
plt.show()


print('-'*50)
# 12. 임의의 웹사이트로부터 데이터 추출 -> 전처리 -> 시각화
school_page = requests.get("http://www.gunpo-ebiz.hs.kr/main.php")
# print(school_page)
# print(school_page.status_code)
# print(school_page.content) # html / 페이지 소스코드
soup2 = BeautifulSoup(school_page.content, 'html.parser')
soup2.prettify()
print(soup2.find_all('span'))
print('-'*100)
for i in range(3,15):
    print(soup2.find_all('span')[i].get_text())
