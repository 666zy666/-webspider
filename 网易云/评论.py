import execjs
import time
from concurrent.futures import  ThreadPoolExecutor
import re

with open("1.js", mode="r", encoding="utf-8") as f:
    exec_js = f.read()
exec_code = execjs.compile(exec_js)

# i0x= {
#     "rid": "R_SO_4_2697934851",
#     "threadId": "R_SO_4_2697934851",
#     #页码
#     "pageNo": num,
#     "pageSize": "20",
#     "cursor": d,
#     "offset": "0",
#     "orderType": "1",
#     "csrf_token": ""
# }

import requests

cookies = {
    'vinfo_n_f_l_n3': 'c0d983269aaef8ff.1.3.1745496259182.1745583869717.1745588154700',
    'csrfToken': 'RTPHoxubJkT6Dpc26HTZZTXN',
    'NMTID': '00ONZ1vkSPYOdnC1k3vnnuigdXf0NkAAAGWqWuAog',
    'JSESSIONID-WYYY': 'UX0Kxwu73Ucg4R%2B%2FewhHde5xsT9RK%5CiFfW%5Cn8A400D8h7ef%5CVGbdwMKEF%2Fg%2B2RIvzTGPgMh4%5CDuBGVjEAysl8Bl7v6Xe2B%2FS3g5cfgKAin9sqZfHUTNlPkVACS5hjnGeJ9UlX39kEgceoMy92hMnGrn8Rc7KbAuQ6WJbGyGz3K%2BV%2FpIM%3A1746601007092',
    '_iuqxldmzr_': '32',
    '_ntes_nnid': 'e2006ba76c3ada9296a3591f90f61dda,1746599207106',
    '_ntes_nuid': 'e2006ba76c3ada9296a3591f90f61dda',
    'WEVNSM': '1.0.0',
    'WNMCID': 'xnolse.1746599208670.01.0',
    '__snaker__id': 'j2pIQATKGKrsteYY',
    'WM_NI': 'QEP%2FTeXzXL0nUR2kJ8615yF5wBf%2BQgopZcxBdxrsLtLv%2BJ7vsI3RGGQnixoSS8z6JyUFAtJpDUdI3QhcopJwE7B8lRaa%2FfEqZ4DJSPR3dHdXlVOiARDRHD8SLM6%2BRYpKTVc%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6eeabf5748e88ad97f03497a88bb2d84b839b9bb1c76ba1ee8887d03d87a89e8dd32af0fea7c3b92a939ba0d0d76f9ca698adb366978efe8cc934f6effb9ac53fb59eaaccd46dadb09684fb4aa8a8be94cf8090aae5abb67eb197fdb3c64d93b2a799ee5991e8b6d7c973979a8f95c97c888bacaab25bacbda191c97d87e98ed9ef5aa3bfe187c87b9aec8cabd25c92edaca9e754b08a818ac45a888e88a5bb599093faccd153b4959cb7e237e2a3',
    'WM_TID': 'kWciN2bPo%2FdEUVVFQAaWON3SPI7BwQkb',
    'gdxidpyhxdE': 'WDBhCTTIn1blDZePM3t26HImqB9EdUdvS7KdYovCE35IA2%2BYbpp7L2q%5C7zIHZCV4oqEUyrQ%2B9E%2BKEsLg5vw4TBPRjMioW2aYrNlA1L0u2Y%2BC%2FsYUY0filmIZCJbvv%2Bng%2BVgbdWN4zHDRjy9a4in8WqfqEPurnNXWKL8p3eHKswqweczR%3A1746600109055',
    'sDeviceId': 'YD-3SrC09Y86N5BVgUVRUPTPM2GeN%2BFmQRA',
    'ntes_utid': 'tid._.xIF2LRurqE9EBlEAERKXLYnDbYqB3QVB._.0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://music.163.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://music.163.com/song?id=2697934851',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    # 'cookie': 'vinfo_n_f_l_n3=c0d983269aaef8ff.1.3.1745496259182.1745583869717.1745588154700; csrfToken=RTPHoxubJkT6Dpc26HTZZTXN; NMTID=00ONZ1vkSPYOdnC1k3vnnuigdXf0NkAAAGWqWuAog; JSESSIONID-WYYY=UX0Kxwu73Ucg4R%2B%2FewhHde5xsT9RK%5CiFfW%5Cn8A400D8h7ef%5CVGbdwMKEF%2Fg%2B2RIvzTGPgMh4%5CDuBGVjEAysl8Bl7v6Xe2B%2FS3g5cfgKAin9sqZfHUTNlPkVACS5hjnGeJ9UlX39kEgceoMy92hMnGrn8Rc7KbAuQ6WJbGyGz3K%2BV%2FpIM%3A1746601007092; _iuqxldmzr_=32; _ntes_nnid=e2006ba76c3ada9296a3591f90f61dda,1746599207106; _ntes_nuid=e2006ba76c3ada9296a3591f90f61dda; WEVNSM=1.0.0; WNMCID=xnolse.1746599208670.01.0; __snaker__id=j2pIQATKGKrsteYY; WM_NI=QEP%2FTeXzXL0nUR2kJ8615yF5wBf%2BQgopZcxBdxrsLtLv%2BJ7vsI3RGGQnixoSS8z6JyUFAtJpDUdI3QhcopJwE7B8lRaa%2FfEqZ4DJSPR3dHdXlVOiARDRHD8SLM6%2BRYpKTVc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeabf5748e88ad97f03497a88bb2d84b839b9bb1c76ba1ee8887d03d87a89e8dd32af0fea7c3b92a939ba0d0d76f9ca698adb366978efe8cc934f6effb9ac53fb59eaaccd46dadb09684fb4aa8a8be94cf8090aae5abb67eb197fdb3c64d93b2a799ee5991e8b6d7c973979a8f95c97c888bacaab25bacbda191c97d87e98ed9ef5aa3bfe187c87b9aec8cabd25c92edaca9e754b08a818ac45a888e88a5bb599093faccd153b4959cb7e237e2a3; WM_TID=kWciN2bPo%2FdEUVVFQAaWON3SPI7BwQkb; gdxidpyhxdE=WDBhCTTIn1blDZePM3t26HImqB9EdUdvS7KdYovCE35IA2%2BYbpp7L2q%5C7zIHZCV4oqEUyrQ%2B9E%2BKEsLg5vw4TBPRjMioW2aYrNlA1L0u2Y%2BC%2FsYUY0filmIZCJbvv%2Bng%2BVgbdWN4zHDRjy9a4in8WqfqEPurnNXWKL8p3eHKswqweczR%3A1746600109055; sDeviceId=YD-3SrC09Y86N5BVgUVRUPTPM2GeN%2BFmQRA; ntes_utid=tid._.xIF2LRurqE9EBlEAERKXLYnDbYqB3QVB._.0',
}

params = {
    'csrf_token': '',
}
# d = time.time()
# d =str(round(d,3)).replace('.','')
# #
# num = 1
# i0x = {
#         "rid": "R_SO_4_2697934851",
#         "threadId": "R_SO_4_2697934851",
#         # 页码
#         "pageNo": num,
#         "pageSize": "20",
#         "cursor": d,
#         "offset": "0",
#         "orderType": "1",
#         "csrf_token": ""
#     }
# data = exec_code.call("l", i0x)
# data['params']=data.pop('encText')
# response = requests.post(
#         'https://music.163.com/weapi/comment/resource/comments/get?csrf_token=',
#         params=params,
#         cookies=cookies,
#         headers=headers,
#         data=data,
#     )
def func(i0x):
    d = time.time()
    d = str(round(d, 3)).replace('.', '')
    #
    i0x["cursor"]=d
    data = exec_code.call("l", i0x)
    data['params'] = data.pop('encText')
    response = requests.post(
        'https://music.163.com/weapi/comment/resource/comments/get?csrf_token=',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    r = response.json()
    obj = re.compile(r"'content': '(.*?)', 'richContent': (.*?), '")
    res = obj.findall(str(r))
    print(res)




    # print(num, response.json())
if __name__ == "__main__":
    #多线程
    with ThreadPoolExecutor(10) as t:
        for num in range(1,100):
            i0x = {
                #歌曲id
                "rid": "R_SO_4_2698782537",
                #歌曲id
                "threadId": "R_SO_4_2698782537",
                # 页码
                "pageNo": num,
                "pageSize": "20",
                "cursor": '',
                "offset": "0",
                "orderType": "1",
                "csrf_token": ""
            }
            t.submit(func,i0x)


