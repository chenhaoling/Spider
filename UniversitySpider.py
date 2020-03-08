# 静态定向爬虫
# 爬取中国大学排名

import requests
from bs4 import BeautifulSoup
import bs4
# 定义从网页获取信息的函数
def getHTMLText(url):
  try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text
  except:
    return ''

# 将获取大学信息填充到列表
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
      if isinstance(tr,bs4.element.Tag):
        tds = tr('td')
        ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])

# 打印数据
def printUnivList(ulist,num):
  for u in ulist:
    print("University:" + u[1] + " " + "Location:" + u[2] + " " + "Score:" + u[3] + "\n")

def main():
  uinfo = []
  url = 'http://zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
  html = getHTMLText(url)
  fillUnivList(uinfo,html)
  printUnivList(uinfo,len(uinfo))
main()