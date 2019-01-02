import matplotlib.pyplot as plt
import numpy as np

#가로 막대 바
# fig, ax= plt.subplots()
# people=('Tom','Doic','Harry','Slim','Jim')
# y_pos=np.arange(len(people))
# performance=3+10*np.random.rand(len(people))
# error=np.random.rand(len(people))
# print(performance)
# # 0~1사이의 5개의 난수 생성한 다음 수식연산 결과를 error에 저장
# ax.barh(y_pos, performance, xerr=error, align='center',
#           color='green', ecolor='red') #수평 방향의 bar차트를 그릴 때 사용
# #ecolor 에러의 색상, align : 가운데 맞춤
# ax.set_yticks(y_pos)
# ax.set_yticklabels(people)
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')
# ax.invert_yaxis() #y값을 위아래를 바꿈
# plt.show()
#y_pos는 각 bar가 그려진 위치, performace는 각 bar에 대한 수치

# print(np.random.rand(5))
#()안에 있는건 랜덤수 개수!, 0~1사이의 난수 발생시킴

# print(type(people))
# print(y_pos)

# #그래프 색상 채우기-1
# x=np.linspace(0,1,500) #0~1사이 일정간격으로 500개로 나눔
# y=np.sin(4*np.pi*x)*np.exp(-5*x)
# fig, ax=plt.subplots()
# ax.fill(x,y, zorder=10) #그래프가 여러개일때 , zorder가 큰순서대로 보여줌
# ax.grid(True, zorder=50)
# plt.show()

#그래프 색상 채우기 -2
# x=np.linspace(0, 2*np.pi,500)
# y1=np.sin(x)
# y2=np.sin(3*x)
#
# fig, ax=plt.subplots()
# ax.fill(x,y1, 'b',x,y2,'r',alpha=0.3)
# #alpha는 투명도 0에 가까울 수록 투명, 1에 가까울수록 불투명
# plt.show()

# from numpy.random import rand
#
# fig, ax=plt.subplots()
# for color in ['red', 'green','blue']:
#     print(color)
#     n=700
#     x,y=rand(2,n) #2행 n열 만큼 난수 생성
#     #각각의 x,y 값에 들어감
#     scale=200.0*rand(n)
#     ax.scatter(x,y ,c=color, label=color, s=scale,alpha=0.3,
#                edgecolor="none")
# ax.legend()
# ax.grid(True)
# plt.show()
    # print("x:")
    # print(x)
    # print("y:")
    # print(y)

# 평균, 분산: 평균에서 떨어져 있는 거리, 0에 가까우면-> 평균 근처를 의미
# 표준편차 : 분산에 대한 제곱근
# 분산: 면적, 표준편차: 길이
# ex) 1,1,5,7,8,8의 표준편차?
# 평균:5
# 분산(평균과의 차이):4, 4, 0 ,2, 3, 3
# 평균과의 차이의 제곱: 16,16,0,4,9,9
# 평균과의 차이의 제곱의 합: 54
# 평균과의 차이의 제곱의 평균: 9(분산)
# 평균과의 차이의 제곱의 합의 평균의 제곱근 : 3 (표준편차)
# 최소값 0% ,Q1(quartile, 1사분위수, 25% 위치 데이터),
# 중위수(m, 50%위치 데이터), Q3(quartile, 3사분위수, 75%위치 데이터)
# 최대값(Q4 4사분위수, 100%위치 데이터)
# 최대값-최소값 = range
# Q3-Q1(Q3에서 Q1까지의 거리) = IQR
# Q1= 1/4*(n+1)   , Q3 = 3/4*(n+1)
# upper fence를 넘어간 값: 이상치 ->
# 이상치를 제거해 의미있는 결과를 얻어냄
# ==>BOXPLOT으로 출력
# http://techntalk.tistory.com/87
# Boxplot 에 대한 설명

np.random.seed(123)
# seed () 속에 123은 옆사람하고 동일한 난수가 나오게함
# seed 값이 같으면 난수가 동일하게 나옴
alldata=[np.random.normal(0 , std , 5) for std in range(1,4)]
print(alldata)

    # print(np.random.normal(0,std,5))
                        #평균, 표준편차, 난수
#normal : 정규분포, 평균을 기준으로 대칭을 이룸
#표준편차가 ..1.2...3으로 점점 커지므로 숫자가 더 둘쑥날쑥해짐

fig, axes=plt.subplots(nrows=1, ncols=2, figsize=(9,4))

