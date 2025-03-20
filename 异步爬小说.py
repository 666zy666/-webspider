import asyncio
import aiohttp
import requests
from lxml import etree
import aiofiles

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }


def get_url(url):

    resp = requests.get(url,headers=headers)
    et = etree.HTML(resp.text)
    url_book = et.xpath("//div[@class='book_last']/dl/dd/a/@href")
    url_book.remove("#footer")
    return url_book

async def download(url_list):
    tasks = []
    for url_href in url_list:
        href_show = "https://m.biqulu.cc"+url_href
        t = asyncio.create_task(download_one(href_show))
        tasks.append(t)
    await asyncio.gather(*tasks,return_exceptions=False)
async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as resp:
            pager = await resp.text()
            et = etree.HTML(pager)
            title = et.xpath("//title/text()")[0].strip()
            pager_source = et.xpath("//div[@id='chaptercontent']/text()")
            print(title)
            print(pager_source)

def main():
    url = "https://m.biqulu.cc/book/6735/list.html"
    url_list = get_url(url)
    asyncio.run(download(url_list))



if __name__ == "__main__":
    main()



