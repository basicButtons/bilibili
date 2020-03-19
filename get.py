import csv
import time
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

for i in range(93596278,93606278):
    con = []
    with open("/Users/maxuan/Desktop/course/1/python/bilibili/txt/"+str(i)+".txt","r",encoding="utf-8") as f:
        file = f.read()
    soup = BeautifulSoup(file,"html.parser")
    try:
        
        title = soup.find("span",class_="tit").text
        #得到标题
        
        
        infos = soup.find("span",class_="a-crumbs").find_all('a')
        tminfo = "主页"
        for info in infos:
            tminfo += '-'+info.text
        #以上是为了得到板块
        
        
        
        container = soup.find("span",class_="a-crumbs").next_sibling
        time_up = container.text
        #以上是为了得到上传时间、
        
        
        
        container = soup.find("div",class_=["default-btn","follow-btn","b-gz","not-follow"])
        fans = container.find("span").find("span").text
        
        
        
        tags=soup.find("li",class_="tag").find_all("a")
        if len(tags) >= 3:
            tag1 = tags[0].text
            tag2 = tags[1].text
            tag3 = tags[2].text
        elif len(tags) ==2:
            tag1 = tags[0].text
            tag2 = tags[1].text
            tag3 = ""
        elif len(tags) ==1:
            tag1 = tags[0].text
            tag2 = ""
            tag3 = ""
        else:
            tag1 = ""
            tag2 = ""
            tag3 = ""
        
        
        mid = soup.find("a",{"report-id":"name"})["href"][21:]

        
        res_1 = requests.get("https://api.bilibili.com/x/web-interface/archive/stat?aid="+str(i),headers=headers)

        
        res_1=res_1.json()["data"]
        
        
        click = res_1["view"]
        
        
        danmu = res_1["danmaku"]

        
        common = res_1["reply"]
        
        
        coins = res_1["coin"]
        
        
        share = res_1["share"]
        
        
        favourites = res_1["favorite"]

        
        now_rank = res_1["now_rank"]
        
        
        his_rank = res_1["his_rank"]

        
        res_2 = requests.get("https://api.bilibili.com/x/player/pagelist?aid="+str(i)+"&jsonp=jsonp",headers=headers)
        
        
        res_2=res_2.json()["data"][0]
        
        
        cid = res_2["cid"]
        
        
        duration = res_2["duration"]
        
        
        rec_add_time = str(time.time())
        
        
        with open("/Users/maxuan/Desktop/course/1/python/bilibili/b.csv","a",encoding="utf-8") as f:
            writer = csv.writer(f)

            con.append(i)
            con.append(i)


            con.append(cid)


            con.append(title)


            con.append(tminfo)


            con.append(time_up)


            con.append(click)


            con.append(danmu)


            con.append(coins)


            con.append(favourites)

            

            con.append(duration)


            con.append(mid)


            con.append(fans)


            con.append(tag1)


            con.append(tag2)


            con.append(tag3)


            con.append(common)


            con.append(share)


            con.append(his_rank)


            con.append(now_rank)
            
            
            con.append(rec_add_time)

            writer.writerow(con)

        print(1)
    except:
        print(2)
        continue
        
