import numpy as np
import matplotlib.pyplot as plt
# data=[5,10,30,20,7,8,10,10]
# label=['A','B','C','D','E','F','G','H']
# plt.pie(data, labels=label)
# #반시계방향, 오른쪽부터
# plt.show()

# data=np.random.randn(1000)
# f, (ax1, ax2)=plt.subplots(1,2,figsize=(6,3))
# # print(data)
# ax1.hist(data, bins=30 , normed = True, color='b')
# ax2.hist(data, bins=30 , normed = True, color='r',cumulative=True)
#                         #normed=True : 전체 합이    #cumulative 누적됨

#loc: 평균, scale:표준편차 , size:데이터 개수
# swap1=np.random.normal(loc=0, scale=1, size=100)
# swap2=np.random.normal(loc=1, scale=2, size=100)
# swap3=np.random.normal(loc=0.3, scale=1.2, size=100)
# f, ax=plt.subplots(1,1,figsize=(5,4))
# ax.boxplot((swap1,swap2,swap3))
# ax.set_xticklabels(['grade1', 'grade2','grade3'])
# plt.show()

# #이미지 생성!!!!! - 히트 맵
# #0~1사이의 난수 3*3생성
# a=np.random.random((3,3))
# plt.imshow(a)
# plt.hot()
# #따뜻한 색깔
# plt.colorbar()
# # print(a)
# plt.show()

import matplotlib.image as mping

# # 이미지 가져오기 : png파일로 저장된거 컨트롤 시,컨트롤 브이 해서
# # BigData파일에 복붙 , 파일명대로 읽어오기 !
# img=mping.imread("아메리카노.png")
# plt.imshow(img)
# plt.hot()
# plt.colorbar()
# # plt.axis('off')
# #축없애기
# plt.show()

#텍스트 출력!

# txt=plt.text(0, 0, "bottom-left corner")
# txt1=plt.text(1, 1, "top-right corner",va='center',ha='center')
#                                     #텍스트 정렬
# plt.show()

# mu, sigma=100,15
# x=mu+sigma*np.random.randn(100000)
# plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# #60, 0.25자리에 출력
# plt.grid(True)
# plt.show()

#하나의 화면에 그래프 여러개 그리기 위해서는 figure함수
# 를 사용해서 Figure객체를 생성
# f1=plt.figure()
# plt.subplot(221)
# plt.subplot(222)
# plt.subplot(212)

# plt.figure(1)
# plt.subplot(211)
# plt.plot([1,2,3])
# plt.subplot(212)
# plt.plot([4,5,6])
#
# plt.figure(2)
# plt.subplot(211)
# plt.plot([4,5,6])
# plt.title('easy~!')

# fig=plt.figure()
# ax1=fig.add_subplot(211)
# ax2=fig.add_axes([0.1, 0.1, 0.7, 0.3])

plt.style.use('bmh')

from numpy.random import beta
def plot_beta_hist(ax, a,b):
    ax.hist(beta(a,b ,size=10000), histtype="stepfilled",
        bins=25, alpha=0.8, normed=True)

fig, ax= plt.subplots()
plot_beta_hist(ax,10,10)
plot_beta_hist(ax,4,12)
plot_beta_hist(ax,50,12)
plot_beta_hist(ax,6,55)
ax.set_title('style sheet')

plt.show()














