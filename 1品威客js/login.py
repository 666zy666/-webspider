# import subprocess
# from functools import partial
# subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs
import requests
import json

import time
import requests
import execjs
import ddddocr
with open(r"C:\Users\郑曦\PycharmProjects\pythonProject1\1品威客js\js.js", mode="r", encoding="utf-8") as f:
    exec_js = f.read()
exec_code = execjs.compile(exec_js)
D=str(int(time.time()))
M={}
# 调用 JavaScript 中的 test 函数，传入参数并打印结果
headers = exec_code.call("fn", M)


params = {
    'channel': 'common_channel',
    'base64': '1',
}
cookies = {
    'XDEBUG_SESSION': 'XDEBUG_ECLIPSE',
    'HWWAFSESID': 'fe00b73cf13681d906',
    'HWWAFSESTIME': '1746087590981',
}

header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.epwk.com/login.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'XDEBUG_SESSION=XDEBUG_ECLIPSE; HWWAFSESID=fe00b73cf13681d906; HWWAFSESTIME=1746087590981',
}
session = requests.session()
res = session.get("https://www.epwk.com/api/epwk/v1/index/time/",cookies=cookies,headers=header)
response = session.get('https://www.epwk.com/api/epwk/v1/captcha/show', params=params, headers=headers)
content = response.json()
base = content['data']['base64']
ocr= ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(base)
url='https://www.epwk.com/api/epwk/v1/user/login'
data = {
    "code": code,
    "hdn_refer": "",
    "password": "111",
    "username": "111",
}
session.headers = exec_code.call("fn", data)
session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
resp = session.post(url, data=data)
print(resp.text)

