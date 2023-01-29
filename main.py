import urllib
import urllib.request
import requests
from lxml import etree

def gethtmls(url):
    global title
    global text
    content = requests.get(url,proxies=proxy).text
    htmls = etree.HTML(content)
    xpath_title = '//meta[@name="keywords"]/@content'
    xpath_text = '//article[@id="nr"]/text()'
    xpath_url = '//a[@class="dise"]/@href'
    title = htmls.xpath(xpath_title)
    text = htmls.xpath(xpath_text)
    url_last = htmls.xpath(xpath_url)
    return url_last[2]

def writein():
    global title
    global text
    fq = open('武斗系教师的日常生活.txt','a',encoding='utf-8')
    if '_' in url:
        fq.write(f'{title}\n')
    for line in text:
        fq.write(f'{line}\n')
    fq.close()

def url_makein(url_last):
    url_final = f'http://www.wenshulou.cc{url_last}'
    return url_final
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    global title
    global text
    open('武斗系教师的日常生活.txt','w',encoding='utf-8')
    url = 'http://www.wenshulou.cc/637/637908/9547769_2.html'
    proxy = {
        'https':'https://113.124.86.24:9999'
    }
    number = int(input('要下载的页数'))
    for n in range(number):
        url_last = gethtmls(url)
        url = url_makein(url_last)
        writein()


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
