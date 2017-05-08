# coding: utf-8
import urllib2
from bs4 import BeautifulSoup
import sys

# 重新设置编码为utf-8格式，否则读取数据汉字会报错
# from csvreader import MyReader
reload(sys)
sys.setdefaultencoding('utf-8')

list2 = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(list2)):
    print(list2[i])
