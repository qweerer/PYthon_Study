'''
使用urllib.request请求一个网页，并打印
'''
from urllib import request

if __name__ == '__main__':

    url = 'http://www.baidu.com/s?ie=UTF-8&wd=python%20word%20%E7%88%AC%E8%99%AB'
    rsp = request.urlopen(url)
    html = rsp.read()
    # html为bytes流，需要解码
    html = html
    print(html)