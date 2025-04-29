import time
import execjs
import requests
with open("js.js", mode="r", encoding="utf-8") as f:
    exec_js = f.read()
exec_code = execjs.compile(exec_js)
D=str(int(time.time()))
U={
    "App-Ver": "",
    "Os-Ver": "",
    "Device-Ver": "",
    "Imei": "",
    "Access-Token": "",
    "Timestemp": D,
    "NonceStr": "1745921263fdww0",
    "App-Id": "4ac490420ac63db4",
    "Device-Os": "web",
    "Signature": "GxVK4R5KanOTW7YdaOsI427JxkjLV4+7DEOJ39g3H6BmQydWxHF/de1ZIuzkgZEf"
}
M={
    "username": "qwqw",
    "password": "qwqw",
    "code": "",
    "hdn_refer": "https://www.epwk.com/"
}
C='a75846eb4ac490420ac63db46d2a03bf'
# 调用 JavaScript 中的 test 函数，传入参数并打印结果
result = exec_code.call('h',U,M,C)

cookies = {
    'Hm_lvt_3PeMcXBypTMJrVhFndZ19WzpWRLFKvg7te': '1745920335',
    'HMACCOUNT': 'CFD8D7C57161D566',
    'HWWAFSESID': 'fb527735e8783d7077',
    'HWWAFSESTIME': '1745920248513',
    'PHPSESSID': '7aa393c37541de5a0218162551dc8b737ce91d14',
    'time_diff': '87',
    'XDEBUG_SESSION': 'XDEBUG_ECLIPSE',
    'banners_show_cookie_ip': '218.19.30.100',
    'adbanner_city': '%E5%B9%BF%E5%B7%9E%E5%B8%82',
    'login_referer': 'https%3A%2F%2Fwww.epwk.com%2F',
    'Hm_lpvt_3PeMcXBypTMJrVhFndZ19WzpWRLFKvg7te': '1745920338',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Access-Token': '',
    'App-Id': '4ac490420ac63db4',
    'App-Ver': '',
    'CHOST': 'www.epwk.com',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Device-Os': 'web',
    'Device-Ver': '',
    'Imei': '',
    'NonceStr': '1745920268av3u3',
    'Origin': 'https://www.epwk.com',
    'Os-Ver': '',
    'Pragma': 'no-cache',
    'Referer': 'https://www.epwk.com/login.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Signature': result,
    'Timestemp': D,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'X-REQUEST-ID': '65f2dca1cc94e02af55aaf3e60b6ab85',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'Hm_lvt_3PeMcXBypTMJrVhFndZ19WzpWRLFKvg7te=1745920335; HMACCOUNT=CFD8D7C57161D566; HWWAFSESID=fb527735e8783d7077; HWWAFSESTIME=1745920248513; PHPSESSID=7aa393c37541de5a0218162551dc8b737ce91d14; time_diff=87; XDEBUG_SESSION=XDEBUG_ECLIPSE; banners_show_cookie_ip=218.19.30.100; adbanner_city=%E5%B9%BF%E5%B7%9E%E5%B8%82; login_referer=https%3A%2F%2Fwww.epwk.com%2F; Hm_lpvt_3PeMcXBypTMJrVhFndZ19WzpWRLFKvg7te=1745920338',
}

data = {
    'username': 'qwqw',
    'password': 'qwqw',
    'code': '',
    'hdn_refer': 'https://www.epwk.com/',
}
response = requests.post('https://www.epwk.com/api/epwk/v1/user/login', cookies=cookies, headers=headers, data=data)

print(response.text)