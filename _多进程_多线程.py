from multiprocessing import Process,Queue
import requests
from lxml import etree
from concurrent.futures import  ThreadPoolExecutor
def get_src(q):
    url = "https://movie.douban.com/top250"
    headers ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }
    resp = requests.get(url,headers=headers)
    resp.encoding = "utf-8"
    et = etree.HTML(resp.text)
    et_url = et.xpath("//div[@class='item']/div[@class='pic']/a/img/@src")
    b = et_url[0]
    q.put(b)
    print("ok2")

def download(url):

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"

    }
    name = url
    print(name)
    resp = requests.get(url,headers=header).content
    print("start1")
    with open(".img_.jpg", mode="wb") as f:
         print("start2")
         f.write(resp)
         print("ok")
def download_img(q):
    with ThreadPoolExecutor(1) as t:
        while 1:
         url_img = q.get()
         print(url_img)
         t.submit(download,url_img)
         print("ok1")


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=get_src,args=(q,))
    p2 = Process(target=download_img,args=(q,))
    p1.start()
    p2.start()

