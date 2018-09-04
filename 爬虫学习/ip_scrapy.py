# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 19:16:01 2018

@author: lenovo
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import HTTPError
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

ip_address = input("请输出你的ip地址:")

html = urlopen("http://www.ip138.com/ips138.asp?ip=%s&action=2" % ip_address)
bsObj = BeautifulSoup(html,"lxml")
data = bsObj.find_all('li')


if data ==[]:
    print ("ip地址有误")
else:
    ip_city_op = data[0].string.split('：')[1]
    city = ip_city_op.split('  ')[0]
    op = ip_city_op.split('  ')[1]
    print ('您的IP地址：'+ip_address)
    print ('IP定位城市是：'+city)
    print ('IP运营商是：'+op)
