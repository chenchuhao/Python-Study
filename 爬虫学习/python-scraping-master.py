# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 10:39:27 2018

@author: lenovo
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import HTTPError
#import beautifulsoup4
import urllib.request
import sqlalchemy
import pandas as pd
import time
import gc
from urllib import request 
from urllib import parse
import re
import time

html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read().decode('utf-8'),'html.parser')
bsObj.h1
bsObj.html

#所有类似情形，urlopen 函数都会抛出“HTTPError”异常。我们可以用下面的方式处理这种异常：
try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
    # 返回空值，中断程序，或者执行另一个方案
else:
    print ("")
    # 程序继续。注意：如果你已经在上面异常捕捉那一段代码里返回或中断（break），
    # 那么就不需要使用else语句了，这段代码也不会执行
    
#判断语句检测返回的html 是不是None： 
if html is None:
    print("URL is not found")
else:
    print ("")
# 程序继续
#print(bsObj.nonExistentTag.someTag)

def getTitle(url):
    try:
        html = urlopen(url).read().decode('utf-8')
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html,"html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("http://www.pythonscraping.com/pages/page1.html")

    
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read().decode('utf-8'),"html.parser")        
namelist = bsObj.find_all('span','green')        
print (namelist[0].string)
for name in namelist:
    print (name.get_text())#等价于name.string


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read().decode('utf-8'),"html.parser")
bsObj.div.find_all('img')
for child in bsObj.find('table',{'id':'giftList'}).children:#子标签
    print (child)
    
for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:#兄弟标签
    print (sibling)

print (bsObj.find('img',{'src':'../img/gifts/img4.jpg'}).parent.previous_sibling.get_text())

#正则表达式
images = bsObj.find_all('img',{'src':re.compile('\.\./img/gifts/img[0-9]+\.jpg')})
for image in images :
    print (image)
    

#维基百科
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)
for link in bsObj.find_all('a'):
    if 'href' in link.attrs:
        print (link.attrs['href'])
        
links =[]
for link in bsObj.find('div',{'id':'bodyContent'}).find_all('a',
                      href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        links.append('https://en.wikipedia.org/'+link.attrs['href'])


#采集整个网站数据，set去重
pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html,'html.parser')
    for link in bsObj.find_all('a',href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #我们遇到新网页
                newPage = link.attrs['href']
                print (newPage)
                pages.add(newPage)
                getLinks(newPage)
                
getLinks("")

# 爬去这个列表所有新闻链接  http://news.baidu.com/
pages = set()
def getLinks(pageUrl):
    global pages
    try:
        html = urlopen(pageUrl)
        bsObj = BeautifulSoup(html,'html.parser')
    except HTTPError as e:
        return None
    
    for link in bsObj.find_all('a',href = re.compile("^(http://news.cctv.com/2018/04/13/)")):       
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #我们遇到新网页
                newPage = link.attrs['href']
                print (newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("http://news.cctv.com")



##通过互联网采集数据
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())










