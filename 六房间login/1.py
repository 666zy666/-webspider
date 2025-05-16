import requests
import time
import re
import execjs
with open("六房间.js", mode="r", encoding="utf-8") as f:
    exec_js = f.read()
exec_code = execjs.compile(exec_js)
d = time.time()
d = str(round(d, 3)).replace('.', '')
headers = {
    "accept": "*/*",
    "accept-language": "en,zh-CN;q=0.9,zh;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://v.6.cn/",
    "sec-ch-ua": r"\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": r"\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}
# cookies = {
#     "shrek_reft": "100374%7C174728352741187",
#     "shrek": "B5174722457842709%7C174728352741187%7C100374",
#     "_tracing": "%2Fredian%2F531358.html-head_userpanel%7C%7C%7C%7C"
# }
url = "https://passport.6.cn/sso/prelogin.php"
params = {
    "username": "12345",
    "domain": "v.6.cn",
    "c": "1",
    "_": d
}
response = requests.get(url, headers=headers,  params=params)
res = response.text
obj = re.compile('"nonce":"(.*?)","')
nonce = obj.findall(res)
password = exec_code.call("ln", nonce[0])
print(password)





