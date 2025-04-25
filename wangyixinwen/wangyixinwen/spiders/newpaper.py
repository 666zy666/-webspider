from typing import Any
from wangyixinwen.items import WangyixinwenItem
import scrapy
from scrapy.http import Response
from selenium import webdriver #用于操作浏览器
from  selenium.webdriver.chrome.options import Options#用于设置浏览器
from selenium.webdriver.chrome.service import Service


class NewpaperSpider(scrapy.Spider):
    name = "newpaper"
    # allowed_domains = ["news.163.com",'war.163.com']
    start_urls = ["https://news.163.com"]
    models_urls = []


    def __init__(self):
        # 增加兼容性
        # 忽略证书错误
        q1=Options()
        q1.add_argument('--ignore-certificate-errors')
        # 忽略 Bluetooth: bluetooth_adapter_winrt.cc:1075 Getting Default Adapter failed. 错误
        q1.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 忽略 DevTools listening on ws://127.0.0.1... 提示
        q1.add_experimental_option('excludeSwitches', ['enable-logging'])

        # 创建并启动浏览器
        self.bro = webdriver.Chrome(service=Service(r'C:\Users\郑曦\PycharmProjects\pythonProject1\极验滑块\chromedriver.exe'))
        # 元素隐性等待（设定时间内找到就执行）


    def parse(self, response,**kwargs):
        url_list =  response.xpath('//div[@class="ns_area list"]/ul/li')
        num = [4,5]
        for num_ in num:
            href = url_list[num_].xpath('./a/@href').extract_first()
            self.models_urls.append(href)
        for url in self.models_urls:

            yield scrapy.Request(url=url,callback=self.parse_model)
    def parse_model(self,response):
        div_list = response.xpath('/html/body/div/div[3]/div[3]/div[1]/div[1]/div/ul/li/div/div[@class="data_row news_article clearfix "]')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            page_href = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            item = WangyixinwenItem()
            item['title']=title

            yield scrapy.Request(url=page_href,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self,response):
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        # 将列表内容转换为字符串
        content = "".join(content)
        item = response.meta['item']
        item['page'] = content
        yield item

        # 关闭浏览器对象
    def closed(self, spider):
            self.bro.quit()






            # .xpath('./a/@href').extract_first()




