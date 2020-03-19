import csv
from bs4 import BeautifulSoup
import requests
headers = {
"Accept": "*/*",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
"Connection": "keep-alive",
"Host": "api.bilibili.com",
"Origin": "https://www.bilibili.com",
"Referer": "https://www.bilibili.com/video/av93596328",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-site",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}

for i in range(93596278,93596279):
    with open("/Users/maxuan/Desktop/course/1/python/bilibili/txt/"+str(i)+".txt","r",encoding="utf-8") as f:
        file = f.read()
    soup = BeautifulSoup(file,"html.parser")
    try:
        container = soup.find("div",class_=["default-btn","follow-btn","b-gz","not-follow"])
        fans = container.find("span").find("span").text
        print(fans)
        
    except:
        continue
        
