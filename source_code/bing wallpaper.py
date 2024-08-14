# -*- codeing = utf-8 -*-
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配`
import urllib.request, urllib.error  # 制定URL，获取网页数据
import time

findImgSrc = re.compile(r'.*url[(]["](.*)["][)]')

def main():
    baseurl = "https://cn.bing.com/"
    getData(baseurl)

def getData(baseurl):
    url = baseurl
    html = askURL(url)  # 保存获取到的网页源码
    # 2.逐一解析数据
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div', class_="img_cont"):  # 查找符合要求的字符串
        item = str(item)
        imgSrc = re.findall(findImgSrc, item)[0]
        today = time.localtime(time.time())
        name = str(today[0])+'-'+str(today[1])+'-'+str(today[2])
        print(imgSrc)
        saveImg(imgSrc,name+".webp")

# 得到指定一个URL的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息，向服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    # 用户代理，表示告诉服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def saveImg(url,path):
    urllib.request.urlretrieve(url,path)

if __name__ == "__main__":  # 当程序执行时
    # 调用函数
     main()
    # init_db("movietest.db")
     print("Success！")

