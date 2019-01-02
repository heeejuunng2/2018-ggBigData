from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse
import requests

# url="http://finance.naver.com/marketindex/"
# res=req.urlopen(url)
# soup=BeautifulSoup(res, 'html.parser')
# price=soup.select_one("div.head_info > span.value").string
# print("usd/krw=", price)

# api="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# values={
#     'stnid':'108'
# }
# params=urllib.parse.urlencode(values)
# url=api+"?"+params
# print(url)
# data=urllib.request.urlopen(url).read()
# test=data.decode("utf-8")
# print(test)
#
# r=requests.get("http://www.gunpo-ebiz.hs.kr/theme/HK16/images/global/logo.png")
# with open("test.png","wb") as f: #binary : 2진수
#     f.write(r.content)
# print("saved")

# html="""
# <html><body>
# <h1>스크래핑</h1>
# <p>웹 페이지 긁어오기</p>
# <p>원하는 부분 추출</p>
# </body></html>
# """
#
# soup=BeautifulSoup(html, 'html.parser')
# h1=soup.html.body.h1
# print("h1="+h1.string)
# p=soup.html.body.p #첫번째 p태그만 이렇게 참조하고 나머지는 이렇게 하면 안됨
# print("p="+p.string)
# p2=p.next_sibling.next_sibling #그 밑에있는 거 출력해줌 또다음꺼하려면 p2.next_sibling.next_sibling 이렇게..
# print("p2="+p2.string)

import matplotlib.pyplot as plt
import pandas as pd

# tbl=pd.read_csv("bmi.csv", index_col=2)
# # print(tb1)
# fig=plt.figure()
# ax=fig.add_subplot(1,1,1)
# def scatter(lbl, color):
#     b=tbl.loc[lbl]
#     ax.scatter(b['weight'], b['height'], c=color, label=lbl)
# scatter('fat','red')
# scatter('normal','yellow')
# scatter('thin','purple')
# ax.legend()
# plt.savefig("bmi-test.png")
# plt.show()

import random
fp=open("bmi2.csv","w",encoding="utf-8")
fp.write("height,weight,label\r\n")

def calc_bmi(h,w):
    bmi=w/(h/100)**2
    if bmi<18.5 : return "thin"
    if bmi<25 : return "normal"
    return "fat"

# print(random.randint(50,100)) #50~100사이의 임의의 변수 생성

cnt={"thin":0, "normal":0, "fat":0}
for i in range(30000):
    h=random.randint(120,200)
    w=random.randint(35,100)
    label=calc_bmi(h,w)
    cnt[label]+=1
    fp.write("{0},{1},{2}\r\n".format(h,w,label))
fp.close()
print("ok", cnt)
    # print(h, w)
print("-"*50)

