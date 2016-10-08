# coding: utf-8
import urllib2
from bs4 import BeautifulSoup
import sys
import re

# 重新设置编码为utf-8格式，否则读取数据汉字会报错
# from csvreader import MyReader
reload(sys)
sys.setdefaultencoding('utf-8')

# line = "Cats are smarter than dogs"

joke_content = '老王<br/>和隔壁老王'

matchObj = re.match(r'(.*)<br/>(.*)', str(joke_content), re.M | re.I)

if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No match!!"
    # print '神评 ' + str(i) + comments[i].string
