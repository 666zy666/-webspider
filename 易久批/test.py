import time
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
with open('./1.js',mode = 'r',encoding='utf-8') as f:
    exejs_file = f.read()
exec_code = execjs.compile(exejs_file)
parm = exec_code.call('fn')
xsign= parm['xsign']
xnonce = parm['xnonce']
datetime = parm['datatime']


import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.yijiupi.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.yijiupi.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'UUID': '4dd0d540f9f71aefc37ba7a84c7c94cd',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'appCode': 'ShoppingMallPC',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-platform': '"Windows"',
    'token': '',
    'x-sign': xsign,
    'x-sign-nonce': xnonce,
    'x-sign-timestamp': datetime,
'x-sign-algorithm':'HMAC_SHA_1',
    'x-sign-version': '2.0'
}


data = {
    'currentPage': 1,
    'data': {
        'searchKey': '百事可乐',
        'searchModes': [
            2,
        ],
        'sort': 0,
        'currentPage': 1,
        'pageSize': 25,
        'filterSpecialArea': False,
        'searchSource': 1,
        'searchKeyNotCorrect': False,
        'brandId': '',
    },
    'pageSize': 25,
    'cityId': 402,
    'countyRegionId': '320116',
    'userClassId': 1,
    'userDisplayClass': 0,
    'addressId': '',
    'deviceType': 3,
}
url = 'https://www.yijiupi.com/v58/Product/List'
# url = 'https://www.yijiupi.com/#/index/list'
# url2 = 'https://uatime.yijiupi.com/unix-time'
# session = requests.session()
# res = session.get('https://uatime.yijiupi.com/unix-time')
# print(datetime)
# print(res.text)


response = requests.post(url, headers=headers, params=data)
print(response.text)
print(response)