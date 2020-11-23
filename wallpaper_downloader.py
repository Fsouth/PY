import requests
from lxml import etree
import  re
import time
import random

'''                  获取手机壁纸              '''

headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    }

def getnum(i):
    global result
    url = r"http://service.picasso.adesk.com/v1/vertical/category/4e4d610cdf714d2966000003/vertical?limit=30&skip={}&adult=false&first=0&order=new".format(i*30)
    response = requests.get(url=url,headers=headers).text
    print('获取第{}个界面'.format(i+1))
    time.sleep(1)
    result = re.findall(r'"img": "(.*?)"',response)
    return result

def getimg(m):
    for url in result:
        time.sleep(random.random())
        img = requests.get(url,headers=headers)
        with open(r'./图片/{}.jpg'.format(m),'wb') as f:
            f.write(img.content)
        m+=1
        

for i in range(0,200):
    m = i*30
    getnum(i)
    getimg(m)
