import time
import  requests
from concurrent.futures import ThreadPoolExecutor
#数据抓取
def src(url,data,header,m):
    time.sleep(m)
    resp = requests.post(url, data=data, headers=header)
    dic = resp.json()
    for item in dic['list']:
        prodName = item['prodName']
        avgPrice = item['avgPrice']
        print(prodName, avgPrice)

#数据更新



if __name__ == '__main__':


    url = "http://www.xinfadi.com.cn/getPriceData.html"

    header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
        }

    with ThreadPoolExecutor(3) as t:
             for i in range(1, 3):
                 data = {
                     "limit": "20",
                     "current": "",
                     "pubDateStartTime": "",
                     "pubDateEndTime": "",
                     "prodPcatid": "1187",
                     "prodCatid": "",
                     "prodName": "",

                 }
                 data['current'] = i
                 t.submit(src, url, data, header, i)







