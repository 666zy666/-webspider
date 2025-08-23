import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en,zh-CN;q=0.9,zh;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}
cookies = {
    "Hm_lvt_3PeMcXBypTMJrVhFndZ19WzpWRLFKvg7te": "1755916528",
    "Hm_lpvt_3PeMcXBypTMJrVhFndZ19WzpWRLFKvg7te": "1755916528",
    "zh_choose": "s",
    "XSRF-TOKEN": "eyJpdiI6IjZlTU5TR04rUXViSWwxODFHa2xZWXc9PSIsInZhbHVlIjoiYk11QVBXaUxSNitHQ3lCc3ZjVHdNRVI2N3pPMG5tVGZOOXdKYUlicDZRTEdpVnlBTFNCQ01yNnN4SERDTFpHZEtiVnVYYzNGK1RJd3p6VDMvanJiZVN3Y08yekVqQTF3THI2RlQ1M0hGMU43Z1gzOE5DbDBvMW05aURodUdhUWgiLCJtYWMiOiJhNWZjYjUzMWU2ZjU4ZTJlZmIwNTdlNWI5MjEyZTE3MTQwZTI4NDdmODZiMGQ1MGZjZDc4YzA1Mjg4MWQ4M2NiIn0%3D",
    "laravel_session": "eyJpdiI6ImR3SDFRMjFCb09xc0htQ1QxN3JPNEE9PSIsInZhbHVlIjoidmxONEw4KzgzVkE1MnM4S0NGYm00bGp5WURvSXhtZmxFYk96bHJTRWhDZGxwYWxYZDBKWDBzY3pmU2Jyd1hab1MrQ3JSOFVKOEcxVTJEZ2VZMEJsSGdYeGRlZnBKUEVINmluencxc2E5Wk1oU0laUG53cHgwOXNNQlk1dUZDZEgiLCJtYWMiOiI2NzMwZjY1ZDdkZmZjNDdjYTRiN2YwYTRkZTE1YzIzMDdmMzQ2NDE2NjlkZTY1NzdiZTk0YTJmMzRiZDgzYjEzIn0%3D"
}
url = "https://www.gz.gov.cn/zwgk/fggw/szfwj/index.html"
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
print(response)