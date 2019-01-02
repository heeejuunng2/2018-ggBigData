# 시각화 연습
# matplotlib자료를 차트나 플롯으로 시각화해주는 패키지
# pylab서브패키지 maplotlib패키지 내에 존재, matlab 소프트웨어의 시각화 명령을
# 사용할 수 있는 패키지

import matplotlib as mpl
import matplotlib.pyplot as plt
# 라인플롯: 선 그리는 함수, 데이터가 시간 순서에 따라 변화하는것을 보여주는 것

# plt.plot([10,20,30,40])
#플롯함수 사용해서 리스트가 하나면 y축값으로 설정됨, x값은 리스트 개수
# plt.plot([10,20,30,40],[1,4,9,16]) #(10,1),(20,4)...
#x축 위치를 직접 명시하기 위해 두개의 같은 길이의 리스트에 자료를 넣는다
# plt.plot([10,20,30,40],[1,4,9,16],'rs:')
# : :점선 , D:다이아몬드 h:핵사곤 ,:마커 없음 -:실선 --:긴점선
# 빨간색 네모 --표시 (색상, 마커 , 선스타일 순)
# 생략되어 있다면 디폴트값이 적용됨
# 마커: 데이터의 위치를 나타내는 기호
# plt.show()
#show() : 차트를 출력하는 함수

# plt.plot([10,20,30,40],[1,4,9,16],c="b",lw=5,ls="--",marker="o",
#                         ms=15,mec="g",mew=5, mfc="r")
# plt.show()
# c: 색상, lw:라인너비(라인두깨), ls:라인스타일 , marker:마커, ms:마커크기
# mec:마커의 테두리 색상, mew:테두리너비(테두리 두께) , mfc:마커색상

# plt.plot([10,20,30,40],[1,4,9,16],c="b",lw=5,ls="--",marker="o",
#                         ms=15,mec="g",mew=5, mfc="r")
# plt.xlim(0,50)
# plt.ylim(-10,30)
# plt.show()
# tick: 체크표시, 축상의 위치 표시 지점을 틱이라고 함, 틱에 써진
# 숫자를 틱 라벨이라고 함, 틱라벨은 자동설정, 수동 설정하려면 xticks,yticks사용

import  numpy as np
# x=np.linspace(-np.pi, np.pi,256)
# # linspace 시작부터(-np.pi) , 끝까지(np.pi) 256칸으로 나눔
# # print(x)
# c=np.cos(x)
# plt.plot(x,c)
# plt.xticks([-np.pi, -np.pi/2, 0 ,np.pi/2 , np.pi])
# plt.yticks([-1, 0 , +1])
# plt.show()

# x=np.linspace(-np.pi, np.pi,256)
# # linspace 시작부터(-np.pi) , 끝까지(np.pi) 256칸으로 나눔
# # print(x)
# c=np.cos(x)
# plt.plot(x,c)
# plt.xticks([-np.pi, -np.pi/2, 0 ,np.pi/2 , np.pi]
#            , [r'$-\pi$' , r'$-\pi/2i$' , r'$0$' , r'$+\pi/2$' , r'$+\pi$'])
# plt.yticks([-1, 0 , +1],["Low","Zero","High"])
# plt.grid(True) # False로 바꾸면 선 안생김
# plt.show()

# t=np.arange(0.,5.,0.2)
# print(t)
# plt.plot(t,t,'r--' , t, 0.5*t**2,'bs:', t, 0.2*t**3,'g^-')
#          # x축, y축 ,선설정
# # t**2 : t의 2제곱
# plt.show()

# # 홀드: 하나의 plot명령이 아니라 여러개의 plot명령을
# # 하나의 그림에 겹쳐서 그릴 수 있음
# plt.plot([1,4,9,6],c="b",lw=5,ls="--",marker="o", ms=15,
#             mec="g",mew=5, mfc="r")
# plt.plot([9,16,4,1],c="k",lw=3,ls=":",marker="s", ms=10,
#             mec="m",mew=5, mfc="c")
# plt.show()

# 범례: 여러 개의 선이 있는 경우 , 각 선이 무슨 자료를 의미하는지
# 표시해주는 기능, loc인수를 사용해서 범례를 표현
# x=np.linspace(-np.pi , np.pi , 256)
# c,s=np.cos(x), np.sin(x)
# plt.plot(x,c,ls="--",label="cosine")
# plt.plot(x,s,ls=":",label="sine")
# plt.legend(loc=2) #loc:0~10 uppder left (0이 가장 좋음)
# # 여기서는 2가 best위치인거, 0~10에따라서 위치가 바뀜
# plt.show()

# 파이선의 특이한 문법
# a,b=5,7
# print(a)
# print(b)
# a,b=b,a
# print(a)
# print(b)

# x=np.linspace(-np.pi , np.pi , 256)
# c,s=np.cos(x), np.sin(x)
# plt.plot(x,c,ls="--",label="cosine")
# plt.xlabel("time")
# plt.ylabel("amplitude") #amplitude: 진폭
# plt.title("Cosine Plot")
# plt.show()

# matplotlib에서 그림은 Figure객체, Axes객체, Axis객체로 구성된다
# Figure객체는 한개 이상의 Axes객체를 포함
# 다시, Axes객체는 두개 이상의 Axis객체를 포함
# Figure객체 : 그림 그려지는 종이 (도화지),
# Axes객체(하나의 플롯), Axis객체(가로축, 세로축)

# np.random.seed(0)
# f1=plt.figure(figsize=(10,2))
# plt.plot(np.random.randn(100))
# plt.show()

# print(np.random.randn(100))
#randn: random normal distribution 랜덤 정규 분포(평균이 0, 표준편차가 1)

# Axes객체, subplot 명령
# Figure 내부에 Axes를 생성하려면 subplot명령을 사용해서
# Axes객체를 얻을 수 있음
# 또는 plot명령을 사용해도 자동으로 Axes객체를 생성해줌
# ex) subplot(2,1,2) 2행 1열에서 2번째 행에 그릴 플롯 명

# x1=np.linspace(0.0, 5.0)
# x2=np.linspace(0.0, 2.0)
# y1=np.cos(2*np.pi*x1) * np.exp(-x1)
# y2=np.cos(2*np.pi*x2)
# ax1=plt.subplot(2,1,1)
# plt.plot(x1,y1,'yo--')
# #피큐어 하나에 엑시즈를 2개 넣고 첫번째 위치
# ax2=plt.subplot(2,1,2)
# plt.plot(x2,y2,'r*:')
# plt.show()

# np.random.seed(0)
# plt.subplot(2,2,1) #, 생략하고 (221) 사용도 가능
# plt.plot(np.random.rand(5))
# plt.title("axes 1")
#
# plt.subplot(2,2,2)
# plt.plot(np.random.rand(5))
# plt.title("axes 2")
#
# plt.subplot(2,2,3)
# plt.plot(np.random.rand(5))
# plt.title("axes 3")
#
# plt.subplot(2,2,4)
# plt.plot(np.random.rand(5))
# plt.title("axes 4")
# plt.tight_layout()
# tight_layout은 타이틀이 그래프와 겹치지 않게 알아서 공백 조정해줌
# plt.show()

# subplots 명령으로 복수의 Axes 객체를 동시에 생성
# fig,axes=plt.subplots(2,2)
# print("fig:"+str(fig))
# print("axes:"+str(axes))
#
# np.random.seed(0)
# axes[0,0].plot(np.random.rand(5))
# axes[0,0].set_title("axis 1")
#
# axes[0,1].plot(np.random.rand(5))
# axes[0,1].set_title("axis 2")
#
# axes[1,0].plot(np.random.rand(5))
# axes[1,0].set_title("axis 3")
#
# axes[1,1].plot(np.random.rand(5))
# axes[1,1].set_title("axis 4")
# plt.tight_layout()
# plt.show()

# x,y=3,5
# print(x)
# print(y)

fig,ax0=plt.subplots()
ax0.plot([10,5,2,9,7],'r-',label='y0')
ax0.set_ylabel('y0')
ax1=ax0.twinx()

ax1.plot([100,200,220,180,120],'g:',label='y1')
ax1.set_ylabel('y1')

plt.show()




























