# coding: utf-8
import urllib2
from _ctypes import Union

from bs4 import BeautifulSoup
import sys

# 重新设置编码为utf-8格式，否则读取数据汉字会报错
# from csvreader import MyReader
reload(sys)
sys.setdefaultencoding('utf-8')

try:
    page = 1
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    content = urllib2.urlopen(urllib2.Request(url, headers=headers)).read()
    soup = BeautifulSoup(content, 'html.parser')
    joke_content = soup.find_all('div', class_='content')
    # joke_content = soup.a.
    comments = soup.find_all('div', class_='main-text')
    # for ct in joke_content:
    #     print ct

    # print joke_content[1]

    for i in range(1, len(comments)):
        print joke_content[i + 1]
        # print '神评 ' + str(i) + comments[i].string
    #     print comments[i]
    #     print "\n"


except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
