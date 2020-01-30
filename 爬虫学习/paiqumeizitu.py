# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 22:26:15 2018

@author: lenovo
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import HTTPError
import requests
#import beautifulsoup4
import urllib.request
from urllib.parse import urlparse
import sqlalchemy
import pandas as pd
import time
import gc
from urllib import request 
from urllib import parse
import re
import time
import datetime
import random
import scrapy
import json

#url = "https://www.zhihu.com/question/22918070"
url = "http://www.mzitu.com/all"
html = request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html,'html.parser')
#用Beautiful Soup结合正则表达式来提取包含所有图片链接（img标签中，class=**，以.jpg结尾的链接）的语句  
links = soup.find_all('img',"origin_image zh-lightbox-thumb",src = re.compile('.jpg$'))
# 设置保存图片的路径，否则会保存到程序当前路径  
path = r'C:\Users\lenovo\Desktop\temp\spider_picture'   #路径前的r是保持字符串原始值的意思，就是说不对其中的符号
for link in links:
    print (link.attrs['src'])
    #保存链接并命名，time.time()返回当前时间戳防止命名冲突  
    request.urlretrieve(link.attrs['src'],path+'\%s.jpg' % time.time())  
    

path = r'C:\Users\lenovo\Desktop\temp\meizi_picture'
links = set()
def GetLinks(pageUrl):
    global links
    try:
        url = urlopen(pageUrl)
        bsObj = BeautifulSoup(url,"html.parser")
    except:
        return None
    for picture in bsObj.find('div',{"class":"main-content"}).find_all('a',{"width":"236","height":"354"},src = re.compile('^(http://i.meizitu.net).*(.jpg)$')):
        request.urlretrieve(picture.attrs['src'],path+'\%s.jpg' % time.time())
        print (picture)
    next_page = bsObj.find('a',"next page-numbers").attrs['href']
    if next_page not in links:
        links.add(next_page)
        GetLinks(next_page)
        
GetLinks("http://www.mzitu.com/")
    

url = urlopen("http://www.mzitu.com/all")
bsObj = BeautifulSoup(url,"html.parser")
for picture in bsObj.find('div',class_="postlist").find_all('img',src = re.compile('^(http://i.meizitu.net).*(.jpg)$')):
    request.urlretrieve(picture.attrs['src'],path+'\%s.jpg' % time.time())
    print (picture)


#############################
from urllib import request
from bs4 import BeautifulSoup
import uuid
import time
import DecompressionMethods
src = 'http://www.mzitu.com/all'
mheaders = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

#读取一个网页
def getHtml(url):
    req = request.Request(url,headers=mheaders) #添加headers避免服务器拒绝非浏览器访问
 #   req.AutomaticDecompression = DecompressionMethods.GZip
    page = request.urlopen(req)
    html = page.read()
    return html.decode('utf-8')  # python3 python2版本直接返回html'

def getallUrl(html):
    #构造一个bs对象
    soup = BeautifulSoup(html, 'html.parser')
    #使用bs对象寻找class为all的div 然后再寻找这些div里面的a标签，可能我们需要多试几次才能准确的get
    all = soup.find('div',class_='all').find_all('a')
    for li in all:
        print(li)

getallUrl(getHtml(src))


#############################测试爬取一张主页
######后记：草鱼反爬虫  请勿盗链
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
req = request.Request("http://www.mzitu.com/",headers = headers)
html = urlopen(req)
bsObj = BeautifulSoup(html,'html.parser')
list_img = set()
for picture in  bsObj.find('div',class_="postlist").find_all('img'):
    list_img.add(picture.attrs['src'])
    request.urlretrieve(picture.attrs['src'],path+'\%s.jpg' % time.time())
    print (picture)


