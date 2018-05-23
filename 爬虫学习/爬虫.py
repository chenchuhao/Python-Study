# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 14:41:24 2018

@author: chenchuhao
"""

"""
爬虫流程：
①先由urllib的request打开Url得到网页html文档——
②浏览器打开网页源代码分析元素节点——
③通过Beautiful Soup或则正则表达式提取想要的数据——
④存储数据到本地磁盘或数据库（抓取，分析，存储）
"""


from bs4 import BeautifulSoup
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

def app_category(tag):
    return tag.has_attr('data-track') and tag.has_attr('itemprop')

tag_list = list()

for i in range(1,98):
    web_page = urllib.request.urlopen('http://search.top.chinaz.com/top.aspx?p=2&b=48&s=3&t=hangye'.format(i))
    soup = BeautifulSoup(web_page, 'html.parser')
    for tr in soup.find_all(attrs={'class':'w320 PCop'}):
        tag_list.append(tr.get_text())
        
        
        
        
        
        
        
###自学笔记
"""
urilib的四个模块：
urllib.request:用于获取网页的响应内容
urllib.error:异常处理模块，用于处理异常的模块
urllib.parse:用于解析url
urllib.robotparse:用于解析robots.txt，主要用于看哪些网站不能进行爬取，不过少用
"""


#请求获取网页返回内容
response = request.urlopen('https://movie.douban.com/')
#获取网页返回内容
print (response.read().decode('utf-8'))
#获取状态码
print (response.status)
#获取请求头
print (response.getheaders())
#对请求头进行遍历
for k,v in response.getheaders():
    print (k,'=',v)

#需要一些反爬网站时,我们需要适当地增加请求头进行请求
# 请求头
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
requests = request.Request('https://movie.douban.com/', headers=headers) # 加入自己的请求头更加接近浏览器
# 进行请求,把Request对象传入urlopen参数中
response = request.urlopen(requests)
print(response.read().decode('utf-8'))


#如果网站需要进行登陆，这时需要用到post方法，用上面的也是可以的。代码如下：
data = {'source': 'None',
 'redir': 'https://www.douban.com/',
 'form_email': 'user',
 'form_password': 'passwd',
 'remember': 'on',
 'login': '登录'}
# 将data的字典类型转换为get请求方式
data = bytes(parse.urlencode(data), encoding='utf-8')
requests = request.Request('https://accounts.douban.com/login', headers=headers, data=data, method='POST')
response = request.urlopen(requests)
print(response.read().decode('utf-8'))




#1、爬取简书网站首页文章的标题和文章链接
from urllib import request
from bs4 import BeautifulSoup    #Beautiful Soup是一个可以从HTML或XML文件中提取结构化数据的Python库     
##构造头文件，模拟浏览器访问        
url = "https://www.jianshu.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}  
pag = request.Request(url,headers = headers)
pag_info = request.urlopen(pag).read().decode('utf-8')#打开Url,获取HttpResponse返回对象并读取其ResposneBody 

# 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器 
soup = BeautifulSoup(pag_info,'html.parser')
# 以格式化的形式打印html 
print (soup.prettify)
titles = soup.find_all('a','title')## 查找所有a标签中class='title'的语句
# 打印查找到的每一个a标签的string和文章链接 
    for title in titles: 
        print(title.string) 
        print("http://www.jianshu.com" + title.get('href'))   
#open()是读写文件的函数,with语句会自动close()已打开文件  
with open(r'C:\Users\lenovo\Desktop\temp\titles.txt','a+') as file :
    for title in titles:
        file.write(title.string+'\n')
        file.write("http://www.jianshu.com" +title.get('href')+'\n\n')
        
abstracts = soup.find_all('p','abstract')
with open(r'C:\Users\lenovo\Desktop\temp\abstacts.txt','a+') as file:
    for abstract in abstracts:
        file.write(abstract.string+'\n\n')
        
        
        
        
#2、爬取知乎网站的美女图片链接，并保存到本地
url = "https://www.zhihu.com/question/22918070"
#url = "http://www.mzitu.com/all"
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
    #使用request.urlretrieve直接将所有远程链接数据下载到本地


"""
#根本停不下来，爬取妹子图片practice
#目标抓取网页
url = 'http://www.mzitu.com/all'
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
#读取一个网页
def GetHtml(Url):
    req = request.Request(url,headers = headers)
    pag = request.urlopen(req)
    html = pag.read()
    return html.decode('utf-8','ignore')
#print (GetHtml(url))

#从入口爬取所有的目标链接
def GetallUrl(html):
    soup = BeautifulSoup(html,'html.parser')
    all = soup.find_all('a','all')
    for li in all:
        print (li)
        
GetallUrl(GetHtml(url))
"""









        