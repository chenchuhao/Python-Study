# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 02:06:13 2018

@author: lenovo
"""

from urllib2 import urlopen
import zlib

opener = urlopen('http://projects.fivethirtyeight.com/2016-nba-picks/')
if 'gzip' in opener.info().get('Content-Encoding', 'NOPE'):
    html = zlib.decompress(opener.read(), 16 + zlib.MAX_WBITS)
else:
    html = opener.read()