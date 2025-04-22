from typing import Any
from xiaohua.items import XiaohuaItem
import scrapy
from scrapy.http import Response
from urllib.parse import urljoin

class MeinvSpider(scrapy.Spider):
    name = "meinv"
    allowed_domains = ["tupianzj.com"]
    start_urls = ["https://www.tupianzj.com/bizhi/DNmeinv/"]
    url = "https://www.tupianzj.com/bizhi/DNmeinv/list_77_%d.html"
    num = 2
    def detail_parse(self, response, **kwargs):
        item=response.meta['item']
        item['name'] = response.xpath('//*[@id="container"]/div/div/div[2]/h1/text()').extract_first()
        item['hot'] = response.xpath('//*[@id="container"]/div/div/div[2]/div[1]/label/text()').extract_first()
        yield item
    #解析首页
    def parse(self, response,**kwargs):
        li_list = response.xpath("//ul[@class='list_con_box_ul']/li")
        for li in li_list:
            item = XiaohuaItem()
            href = li.xpath('./a/@href').extract_first()
            href = response.urljoin(href)
            # # self.num += 1
            yield scrapy.Request(url=href,callback=self.detail_parse,meta={'item':item})
        if self.num<=3:
            new_url = format(self.url%self.num)
            self.num += 1
            yield scrapy.Request(url=new_url,callback=self.parse)


