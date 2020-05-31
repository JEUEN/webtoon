import os
import urllib.request

from bs4 import BeautifulSoup

html = urllib.request.urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=733074&weekday=mon")#만화 페이지
soup=BeautifulSoup(html.read(),"html.parser")#페이지 정보를 읽어옴

detail=soup.find("div",{"class":"detail"})#만화명
title=soup.find("td",{"class":"title"})#최신 회차 title

fileName=title.get_text()#웹툰명을 받아옴
folder=detail.get_text()#회차명 받아옴

os.chdir("/Users/김승종/Desktop/웹툰")#디렉토리 이동
# os.mkdir(folder.strip())#웹툰 명 폴더 생성
# os.chdir("/Users/김승종/Desktop/웹툰/"+fileName.strip()) #웹툰 명으로 생성된 디렉토리로 이동
os.mkdir(fileName.strip())#회차정보 폴더 생성

html2=urllib.request.urlopen("https://comic.naver.com"+title["href"])#최신회차로 url 이동
page=BeautifulSoup(html2.read(),"html.parser")#최신회차 페이지 정보를 읽어옴
img=page.findAll("div",{"class":"wt_viewer"})#이미지정보를 읽음

imgUrl=img["src"]

for save in img :
    urllib.request.urlretrieve(imgUrl,imgUrl["alt"]+".jpg")