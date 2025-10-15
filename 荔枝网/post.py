import requests
import json
import subprocess
sign=subprocess.run(['node','1.js',],capture_output=True,text=True).stdout

data=json.loads(sign)

t=str(data["X-ITOUCHTV-Ca-Timestamp"])



headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en,zh-CN;q=0.9,zh;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://www.gdtv.cn",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.gdtv.cn/",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "x-itouchtv-ca-key": data["X-ITOUCHTV-Ca-Key"],
    "x-itouchtv-ca-signature": data["X-ITOUCHTV-Ca-Signature"],
    "x-itouchtv-ca-timestamp": t,
    "x-itouchtv-client": "WEB_PC",
    "x-itouchtv-device-id": "WEB_d8e6e280-9087-11f0-bbd1-41ad82e4d631"
}
import time
datatime= time.time()
d = str(round(datatime, 3)).replace('.', '')

url = "https://gdtv-api.gdtv.cn/api/channel/v1/news"
params = {
    "beginScore": 1758069586000,
    "channelId": "246",
    "pageSize": "11"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)


