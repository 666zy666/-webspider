import time
import requests
import re
import json
from prox_redis import Proxyredis
class IP_save:
    def __init__(self):
        self.pr = Proxyredis()
    def save_ip(self,ips):
        for ip in ips:
            print('redis')
            self.pr.add_ip(ip)


class KUAIDAILIIP(IP_save):
    def __init__(self):
        super().__init__()
        self.session  = requests.session()
        self.session.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en,zh-CN;q=0.9,zh;q=0.8",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "referer": "https://www.kuaidaili.com/free/",
            "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        }
    def run(self):
        time.sleep(5)
        for n in range(1,5):
            data = self.get_one_page_ip(n)
            self.save_ip(data)
            time.sleep(1)
    def get_one_page_ip(self,num):
        url = f"https://www.kuaidaili.com/free/intr/{num}/"
        response = self.session.get(url, headers=self.session.headers)
        print(response)
        # print(response.text)
        obj = re.compile(r'const fpsList = (?P<ip>.*?);', re.S)
        ips = obj.search(response.text).group('ip')
        print(ips)
        ip_list = json.loads(ips)
        results =[]
        for ip_dict in ip_list:
            proxy_ip = ip_dict['ip']+":"+ip_dict['port']
            print(proxy_ip)
            results.append(proxy_ip)
        return results

def run():
    KUAIDAILIIP().run()
if __name__ == "__main__":
    run()









