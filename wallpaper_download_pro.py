import requests
import threading
import queue
import re
import winreg
import os

'''                  获取手机壁纸（高清)      多线程           '''

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}


def get_directory():  # 判断路径是否存在，否的话生成
    global path
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    path = winreg.QueryValueEx(key, "Desktop")[0]+"//pic"
    print(path)
    if not os.path.exists(path):
        os.mkdir(path)


def get_img(img_url):
    response = requests.get(url=img_url, headers=headers).text
    result = re.findall(r'"id": "(.*?)"', response)
    for id in result:
        print(id)
        final_url = r"http://img5.adesk.com/{}?adult=false".format(id)
        img = requests.get(url=final_url, headers=headers)
        with open(path+'/{}.jpg'.format(id), 'wb') as f:
            f.write(img.content)



if __name__ == '__main__':
    get_directory()
    q = queue.Queue()
    for i in range(170):
        url = r"http://service.picasso.adesk.com/v1/vertical/category/4e4d610cdf714d2966000003/vertical?limit=30&skip={}&adult=false&first=0&order=new".format(
            i*30)
        q.put(url)
    while not q.empty():
        for i in range(5):
            t = threading.Thread(target=get_img,args=(q.get(),))
            t.start()