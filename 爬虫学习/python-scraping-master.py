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
import datetime
import random
html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read().decode('utf-8'),'html.parser')
bsObj.h1
bsObj.html

###########2.1异常代码处理 ###############
#（1）所有类似情形，urlopen 函数都会抛出“HTTPError”异常。我们可以用下面的方式处理这种异常：
try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
    # 返回空值，中断程序，或者执行另一个方案
else:
    print ("")
    # 程序继续。注意：如果你已经在上面异常捕捉那一段代码里返回或中断（break），
    # 那么就不需要使用else语句了，这段代码也不会执行
    
#（2）判断语句检测返回的html 是不是None： 
if html is None:
    print("URL is not found")
else:
    print ("")
# 程序继续
#（3）如果继续调用None对象下面的子标签，会发生AttributeError
#以下语句会产生一个None对象，很有必要这样做。不然会报错。
print(bsObj.nonExistentTag)
#例如
print(bsObj.nonExistentTag.someTag)
#如何避免这种情况呢
try:
    badContent = bsObj.nonExistTag.anotherTag
except AttributeError as e:
    print ('Warning:AttributeError--Tag was nont found')
else :
    if badContent == None:
        print ('Warning:None--Tag was not found')
    else:
        print ('badContent')
        
#（4）骚年，看了上面的异常处理，是不是觉得有点麻烦，那我们重新组织以下代码吧
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print ("Title could not be found")
else:
    print (title)

        

###########2.2再端一碗BeautifulSoup###############
#class 是Python 语言的保留字，在Python 程序里是不能当作变量或参数名使用  
#不能这样子：bsObj.findAll(class="green")

#2.2.1　BeautifulSoup的find()和findAll()
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read().decode('utf-8'),"html.parser")        
namelist = bsObj.find_all('span',{'class':'green'})
#namelist = bsObj.find_all('span',class_='green')        
print (namelist[0].string)
for name in namelist:
    print (name.get_text())#等价于name.string

#2.2.2　其他BeautifulSoup对象
#BeautifulSoup 对象 bsObj
#标签Tag 对象  bsObj.div.h1
#NavigableString 对象
#Comment 对象


#2.2.3　导航树
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read().decode('utf-8'),"html.parser")
try：
    bsObj.tag.subTag.anotherSubTag
except:
    pass

"""
孩子（child）和后代（descendant）有显著的
不同：和人类的家谱一样，子标签就是一个父标签的下一级，而后代标签是指一个父标签
下面所有级别的标签。例如，tr 标签是tabel 标签的子标签，而tr、th、td、img 和span
标签都是tabel 标签的后代标签（我们的示例页面中就是如此）。所有的子标签都是后代标
签，但不是所有的后代标签都是子标签。
一般情况下，BeautifulSoup 函数总是处理当前标签的后代标签。例如，bsObj.body.h1 选
择了body 标签后代里的第一个h1 标签，不会去找body 外面的标签。
类似地，bsObj.div.findAll("img") 会找出文档中第一个div 标签，然后获取这个div 后
代里所有的img 标签列表。
"""
#如果你只想找出子标签，可以用.children 标签：

#返回list
bsObj.div.find_all('img')
#返回list[0]
bsObj.div.find('img')
#子标签
for child in bsObj.find('table',{'id':'giftList'}).children:
    print (child)
#兄弟标签 ,跳过标题h   
for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:
    print (sibling)
#找到一组兄弟标签中的最后一个标签， 那么previous_siblings 函数也会很有用。
#还next_sibling和previous_sibling函数，
#next_siblings和previous_siblings的作用类似，只是它们返回的是单个标签，而不是一组标签。

#父标签parent
print (bsObj.find('img',{'src':'../img/gifts/img4.jpg'}).parent.previous_sibling.get_text())





#2.4　正则表达式和beautifulSoup
images = bsObj.find_all('img',{'src':re.compile('\.\./img/gifts/img[0-9]+\.jpg')})
for image in images :
    print (image)
    

#2.5　获取属性
#查找标签对象的属性
#myTag.attrs
bsObj.table.attrs


#2.6　Lambda表达式
bsObj.find(lambda tag :len(tag.attrs)==2)






###########第3章 开始采集###############
#3.1 遍历单个域名   
#获取词条链接list  维基百科
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
"""
links2 = []
for link2 in bsObj.find_all('a',href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link2.attrs:
        links2.append('https://en.wikipedia.org/'+link2.attrs['href'])
"""
#遍历页面
random.seed(datetime.datetime.now())






#3.2采集整个网站数据，set去重
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










