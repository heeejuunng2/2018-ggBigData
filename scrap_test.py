from bs4 import BeautifulSoup
import urllib.request as req

# url="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
# res=req.urlopen(url)
# # print(res)
# soup=BeautifulSoup(res, 'html.parser')
# # print(soup)
# title=soup.find('title').string #.string : 문자만 나오게함
# # print(title)
# wf=soup.find('wf').string
# print(wf)

html="""
<html><body>
<ul>
<li><a href="https://www.naver.com">naver</a></li>
<li><a href="https://www.daum.net">daum</a></li>
</ul>
<div id="test">
    <h1>게임 리스트</h1>
    <ul class="games">
        <li>롤</li>
        <li>배틀그라운드</li>
        <li>메이플스토리</li>
    </ul>
</div>
</body></html>
"""
soup=BeautifulSoup(html, 'html.parser')
links=soup.find_all('a')
print(links)

for a in links:
    href=a.attrs['href']
    text=a.string
    print(text, ">", href)

soup=BeautifulSoup(html, 'html.parser')
h1=soup.select_one("div#test > h1").string
print(h1)




