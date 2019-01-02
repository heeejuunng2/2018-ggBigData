import nltk.corpus
import requests
from bs4 import BeautifulSoup
import matplotlib.image as mping
import matplotlib.pyplot as plt
import numpy as np

def Get_the_page_by_beautifulsoup(): #함수이름
    page=requests.get("https://simplifydatascience.wordpress.com/about/")
    # print(page) #page에 정상적으로 저장되었는지 확인 200나오므로 제대로 저장된거
    #             #403 나오면 오류
    # print(page.status_code) #응답코드 출력 200
    # print(page.content) #html / 페이지 소스코드
    soup=BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    # print(soup.prettify()) #소스코드를 보기좋게 꾸밈(정리 정돈)
    # print(soup.find_all('p')) #출력결과해석 :
    # 데이터타입: 리스트
    # p태그로 나누어져 리스트에 저장
    #웹스크래핑
    # print(soup.find_all('p')[0]) #리스트의 첫번째 요소 출력
    # print(soup.find_all('p')[0].get_text()) #0번째에서 p태크 없이 데이터만 출력

    #-> ★스크래핑:Scrapping★ : 인터넷에서 가져오는거(긁어오는거) -> Web Scrapping

#Mini Project )좋아하는 사이트 -> 특정 자료를 가져와서 출력

def Ger_the_mypage():
    # 옷에대한 정보(사이즈), 및 이미지(사진)
    my_page=requests.get("http://attrangs.co.kr/shop/view.php?index_no=41187&cate=090103")
    # print(my_page)
    # print(my_page.content)
    soup3=BeautifulSoup(my_page.content, 'html.parser')
    soup3.prettify()
    for i in range(9,15):
        print(soup3.find_all('strong')[i].get_text())
    for i in range(70,76):
        print(soup3.find_all('td')[i].get_text())
    #시각화(이미지)
    img=mping.imread("blouse.png")
    plt.imshow(img)
    plt.axis('off')
    plt.show()

#학교홈페이지
def Get_the_schoolpage():
    school_page=requests.get("http://www.gunpo-ebiz.hs.kr/main.php")
    # print(school_page)
    # print(school_page.status_code)
    # print(school_page.content) # html / 페이지 소스코드
    soup2=BeautifulSoup(school_page.content, 'html.parser')
    soup2.prettify()
    # print(soup2.find_all('span'))
    # print('-'*100)
    # for i in range(3,15):
    #     print(soup2.find_all('span')[i].get_text())

if __name__=="__main__":  #메인함수
    Get_the_page_by_beautifulsoup() #함수호출해라
    Get_the_schoolpage()
    Ger_the_mypage()
































