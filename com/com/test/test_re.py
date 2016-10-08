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

joke_content = ''

try:
    page = 1
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    content = urllib2.urlopen(urllib2.Request(url, headers=headers)).read()
    # content = re.sub(r'<br/>', '', str(content))
    content = re.sub(r'<a class=\"contentHerf\" href=\"/article/\d\" target=\"_blank\">', '', str(content))
    content = re.sub(r'<span>', '', str(content))
    content = re.sub(r'\n', '', str(content))
    soup = BeautifulSoup(content, 'html.parser')
    joke_content = soup.find_all('div', class_='article block untagged mb15')
    print joke_content

    for i in range(0, len(joke_content)):
        print joke_content[i].div.strings

        # comments = soup.find_all('div', class_='main-text')
        # matchObj = re.sub(r'(.*)<br/>(.*)', str(joke_content), re.M | re.I)

        # for i in range(1, len(comments)):
        #     print str(i) + '. ' + joke_content[i].string
        # print '神评 ' + comments[i].string + "\n"

except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
