import time

from prox_redis import Proxyredis
import asyncio
import aiohttp


async def check_one(ip,sem,pr):
    try:
        headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.baidu.com/link?url=YT0ZCklNx5Bd_p9hVwXvRbeBS9UxiMUHE9PP8qzoGCcTixDI66YsZMfZnY_k9EaM&wd=&eqid=b4061171002df8320000000668a59106",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
        timeout = aiohttp.ClientTimeout(10)

        async with sem:
            async with aiohttp.ClientSession(timeout=timeout,headers=headers) as session:
                print(2)
                async with session.get(url="https://www.baidu.com/", proxy="http://"+ip) as resp:
                    print(1)
                    await resp.content.read()
                    if resp.status in [200, 302]:
                        pr.set_max_score(ip)
                        print('ok,ip可用',ip)
                    else:
                        pr.desc_score(ip)
                        print('ip,不可用',ip)
    except Exception as e:
        print(e)
        pr.desc_score(ip)
        print('wrong,ip,不可用',ip)



async def check_all(ips,pr):
    sem = asyncio.Semaphore(20)
    tasks = []
    for ip in ips:
        tk = asyncio.create_task(check_one(ip,sem,pr))
        tasks.append(tk)
    await asyncio.wait(tasks)
def run():
    time.sleep(10)
    pr = Proxyredis()
    ips = pr.get_all_ip()
    asyncio.run(check_all(ips,pr))
if __name__ == "__main__":
    run()