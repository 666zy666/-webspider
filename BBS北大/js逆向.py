import requests
import time
import hashlib
pwd = "111"
user = "zhangkai"
url = "https://bbs.pku.edu.cn/v2/home.php"
header = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}
res = requests.get(url,headers=header)
#登录
cookie_dict = res.cookies.get_dict()
ctime = int(time.time())
data_string  = f"{pwd}{user}{ctime}{pwd}"
obj = hashlib.md5()
obj.update(data_string.encode('utf-8'))
md5_string = obj.hexdigest()
data={
'username': 'zhang',
'password': '111',
'keepalive': '0',
'time': ctime,
't':md5_string
}
res = requests.post(
    url='https://bbs.pku.edu.cn/v2/ajax/login.php',data=data,cookies=cookie_dict,headers=header
)
#无账号密码无法完全实现可以通过更改用户名验证js
print(res.text)