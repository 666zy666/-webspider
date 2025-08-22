from redis import Redis
import random
class Proxyredis:
    def __init__(self):
        self.red = Redis(
            host = 'localhost',
            port = 6379,
            db = 0,
            password ='123456',
            decode_responses =True)

    def add_ip(self,ip):
        if not self.red.zrank('proxy_ip',ip):
            print("new ip")
            self.red.zadd("proxy_ip",{ip:10})
            print(ip)
        else:
            print('old ip')
    def get_all_ip(self):
        return  self.red.zrange("proxy_ip",0,-1)


    def set_max_score(self,ip):
        self.red.zadd("proxy_ip",{ip:10})
    def desc_score(self,ip):
        self.red.zincrby("proxy_ip",-2,ip)
        score = self.red.zscore('proxy_ip',ip)
        if score == 0:
            self.red.zrem('proxy_ip',ip)
    def get_good_ip(self):
        ips=self.red.zrangebyscore("proxy_ip",100,100,0,-1)

        if not ips:
            ips = self.red.zrangebyscore("proxy_ip", 1, 100, 0, -1)
            return random.choice(ips)
        return random.choice(ips)





