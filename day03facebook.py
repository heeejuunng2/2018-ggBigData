import sys
import urllib.request
import json
#패키지: 함수들의 묶음

if __name__=='__main__':

    # [CODE 1]
    page_name = "jtbcnews"
    app_id = "1757155681067993"
    app_secret = "a8b0b0dd031ea8dbf4367ada327cc1b8"
    access_token = app_id+"|"+app_secret

    # [CODE 2]
    # https://graph.facebook.com/v2.8/[page_id]/?access+token=[App_ID][Secret_Key]
    # 형식의 문자열을 만들어 낸다

    base = "https://graph.facebook.com/v2.8"
    node = "/"+page_name
    parameters ="/?access_token=%s" % access_token
    url = base + node + parameters
    # print(url)

    # [CODE 3]
    req = urllib.request.Request(url)

    # [CODE 4]
    try:
        respones = urllib.request.urlopen(req)
        if respones.getcode() == 200:
            data = json.loads(respones.read().decode('utf-8'))
            page_id = data['id']
            print("%s Facebook Numeric ID : %s" % (page_name,page_id))
    except Exception as e:
        print(e)

# 시각적 자료!!
# 다운받아야함
import matplotlib.pyplot as plt

#그래프
# plt.plot([1,2,3,4])
# plt.show()
x=range(0,100)
y=[v*v for v in x]
# x: [0,1,2,3,4]
# v: [0,1,4,9,16] v는 x값을 읽어온거임
# print(x)
# print(y)
# plt.plot(x,y, 'ro') #r은 색상, o는 모양
#y 노랑 b파랑 ... s 사각형 o 원 ^, v 삼각형 + 플러스 ...
plt.plot(x,y, 'g.')
plt.show()


# 화면하나를 여러개로 나눌때 사용
fig=plt.figure()
ax1=fig.add_subplot(2,1,1) #2행1열
ax2=fig.add_subplot(2,1,2) #add_subplot하위에 그림을 추가해라 ..?
x=range(0,100)
y=[v*v for v in x]
ax1.plot(x,y)
ax2.bar(x,y) #막대그래프
plt.plot(x,y,color='green',marker='o',linestyle='solid')
plt.title('output')
plt.xlabel('num')
plt.ylabel('numsquare')
plt.show()

import numpy as np
print(np.pi)
x=np.arange(0.0 ,2*np.pi , 0.1)
# 0.0부터 6.2까지 0.1씩 증가시켜라
print(x)
sin_y=np.sin(x)
cos_y=np.cos(x)

# (내생각엔 자리 정해주는 거 아닐까 ... )
fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)

ax1.plot(x, sin_y, 'b--')
ax2.plot(x, cos_y, 'r--')

plt.show()

import matplotlib.pyplot as plt
fig=plt.figure()
print(type(fig))
# ax=fig.add_subplot(2,2,1) #2행 2열에 첫번째칸
fig,ax=plt.subplots(2,2)
ax[1][1].plot([1,2,3,4])
plt.show()