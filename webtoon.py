import os
import urllib.request
from bs4 import BeautifulSoup

#에러제거
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

html = urllib.request.urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=733074&weekday=mon")#만화 페이지
soup=BeautifulSoup(html.read(),"html.parser")#페이지 정보를 읽어옴

name = soup.select("div.comicinfo h2")[0].text.split()#comicinfo클래스 h2태그 중 만화명,작가명 텍스트만 따 배열생성
detail = "".join(name[0])
title= soup.find_all("td",{"class":"title"})#최신 회차 title

os.chdir("C:/Users/user/PycharmProjects/untitled")#디렉토리 이동
os.mkdir(detail)#웹툰 명 폴더 생성
os.chdir("./" + detail)  # 웹툰 명으로 생성된 디렉토리로 이동

for s in title:
    num=1
    folder=s.text.strip()
    os.mkdir(folder)#회차정보 폴더 생성
    os.chdir("./"+folder)
    url="https://comic.naver.com"+s.a['href']#최신회차로 url 이동
    page=urllib.request.urlopen(url)
    comic_page=BeautifulSoup(page.read(),"html.parser")#최신회차 페이지 정보를 읽어옴
    img=comic_page.findAll("img",{"alt":"comic content"})#이미지정보를 읽음
    for save in img :
        urllib.request.urlretrieve(save["src"],str(num)+".jpg")
        num=num+1
    print(folder+"\t saved completely!")
    os.chdir((".."))