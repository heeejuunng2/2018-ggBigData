import matplotlib.pyplot as plt
import numpy as np

# np.random.seed(123)
# alldata=[np.random.normal(0, std, 100) for std in range(1,4)]
#                         #평균, 표준편차, 난수
# fig, axes=plt.subplots(nrows=1, ncols=2, figsize=(9,4))
#                         #한줄에 두칸
# bplot1=axes[0].boxplot(alldata,
#                        vert=True,  #수직/수평 여부
#                        patch_artist=True) #색상 채울지 말지 여부
# bplot2=axes[1].boxplot(alldata,
#                        notch=True, #중앙값의 위치가 볼록 들어감 : 신뢰기관(?)
#                        vert=True,
#                        patch_artist=True)
# colors=['pink','lightblue','lightgreen']
#
# for bplot in (bplot1, bplot2):
#     for patch, color in zip(bplot['boxes'], colors):
#         patch.set_facecolor(color)
#
# plt.show()

# -> 그래프 출력할 때 나오는 빨간줄은 중앙값을 나타냄
# -> 동그라미는 이상치를 나타냄

# np.random.seed(123)
# mu=200 #평균
# sigma=25 #표준편차
# x=np.random.normal(mu, sigma, size=100) #정규분포를 띄는 난수를 생성해라
# # 평균이 200이고 표준편차가 25인 난수 100개를 만들어라
# # print(x)
# fig, (ax0, ax1)=plt.subplots(ncols=2, figsize=(8,4))
# # fig, axes[0],axes[1] 이랑 의미 같음
# ax0.hist(x,bins=100,normed=1, histtype='stepfilled', facecolor='g', alpha=0.75)
# #       (데이터, 구간, 확률분포, 히스토그램 모양, 색깔, 투명도)
# #normed=1 은 히스토그램의 합이 1이 되게 만듬
# # bins=100은 구간을 100으로 나눔
# ax0.set_title('stepfilled')
#
# bins=[100,150,180,195,205,220,250,300]
# ax1.hist(x,bins,normed=1, histtype='bar', rwidth=0.8)
# ax1.set_title('unequal bins')
# plt.show()

# plt.plot([4,5,6,8])
# plt.ylabel('some numbers')

# t=np.arange(0. , 5. , 0.2)
# #0~5까지 0.2씩 증가
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

# a=plt.plot([1,2,3,4])  #출력시 파란그래프
# b=plt.ylabel('some num') #y레이블 지정
# c=plt.xlabel('some num')  #x레이블 지정
# a+=(plt.plot([0.5 , 1.1 , 2.1, 3.4])) #출력시 주황그래프
# print(a)
# print(b)
# print(c)

# a=plt.plot([1,2,3,4])  #출력시 파란그래프
# b=plt.ylabel('some num') #y레이블 지정
# c=plt.xlabel('some num')  #x레이블 지정
# d=plt.plot([0.5 , 1.1 , 2.1, 3.4]) #출력시 주황그래프
# print(a)
# print(b)
# print(c)
# print(d)

# t=np.arange(0. , 5. , 0.2)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g' )
# plt.show()

#seaborn 설치
# plt.plot([1,2,3,4],[1,4,9,6] ,'ro')
# plt.show()

# x1=[1,2,3,4,5]
# y1=[1,4,9,16,25]
# x2=[1,2,4,6,8]
# y2=[2,4,8,12,16]
# plt.plot(x1,y1, 'r', label='first data')
# plt.plot(x2, y2, 'g', label='second data')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.xlim(0.0 , 9.0)
# plt.ylim(0.0, 30.0)
# plt.legend()

# plt.show()

# f, ax= plt.subplots(1 , 1 ,figsize=(5,4))
# print(f, ax)
# x=np.linspace(0 ,10 ,1000)
# y=np.power(x, 2)
# ax.plot(x,y)
# # x=0.01 , x의 제곱 = 0.0001(10의 -4승)
# # 1e-4 = 10의 -4승
# ax.set_xlim((1,5))
# ax.set_ylim((0,30))
# plt.tight_layout()
# plt.show()
# plt.savefig('myplot.png')

# data=np.random.rand(10,2) #10행 2열
# print(data)
# print(data.shape)
# plt.scatter(data[:, 0], data[:,1])
# plt.show()

# x=np.random.rand(10)
# y=np.random.rand(10)
# z=np.sqrt(x**2+y**2)
# # sqrt : square root(제곱근)
# plt.subplot(321)
# plt.scatter(x,y,s=80,c=z,marker='>')
# plt.show()

n=5 #데이터 개수
menMeans=(20,35,30,35,27)
womenMeans=(25,32,34,20,25)
ind=np.arange(n)  #0~4까지

# print(ind)
# plt.bar(ind, menMeans, color='pink')
p1=plt.bar(ind+0.00, menMeans,width=0.3,color='y')
p2=plt.bar(ind+0.33, womenMeans, width=0.3 ,color='r')
plt.xlabel('The number of people')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.legend((p1[0], p2[0]), ('Men', 'Women'))
# width 너비, 폭
plt.show()