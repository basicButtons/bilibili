import requests
from bs4 import BeautifulSoup
import time

for i in range(93596278,93606278):
    url = 'https://www.bilibili.com/video/av' + str(i)
    res = requests.get(url)
    with open("/Users/maxuan/Desktop/course/1/python/bilibili/txt/"+str(i)+".txt","w",encoding="utf-8") as f:
        f.write(res.text)


    
    
