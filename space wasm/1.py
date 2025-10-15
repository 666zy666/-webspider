import time
import requests
import subprocess
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Referer": "https://spa14.scrape.center/page/3",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://spa14.scrape.center/api/movie/"
for i in range(7,10):
    sign=subprocess.run(['node','1.js',str(i*10)],capture_output=True,text=True)
    print(sign)
    sign = sign.stdout.strip()
    params = {
        "limit": "10",
        "offset": str(i*10),
        "sign": sign
    }
    print(sign)
    # time.sleep(2)
    # response = requests.get(url, headers=headers, params=params)
    # print(response.text)
    # print(response)
    # time.sleep(2)