import scrapy
from  scrapy.http.response.html import HtmlResponse
from file.items import FileItem
class FileSpiderSpider(scrapy.Spider):
    name = "file_spider"
    allowed_domains = ["gz.gov.cn"]
    start_urls = ["https://www.gz.gov.cn/zwgk/fggw/szfwj/index.html"]
    def parse(self, res:HtmlResponse,**kwargs):
        li_list = res.xpath('//ul[@class="wjbh_list"]/li/a')
        next_url =res.xpath('//a[@class="next up"]/@href').extract_first()
        for li in li_list:
            url=li.xpath('./@href').extract_first()
            title=li.xpath('./@title').extract_first()
            yield scrapy.Request(url=url,callback=self.detail,meta={
                'category':'市政府文件',
                'title':title,
                "url":url
            })
            # 测试
            # break
        # print(next_url)
        # print(news_list)
        yield scrapy.Request(url=next_url,callback=self.parse)
    def detail(self,res:HtmlResponse):
        pages =res.xpath('//div[@class="content_article"]/p/text()').extract()
        res.meta['content'] = ''.join(pages)
        item = FileItem()
        item['page']=res.meta
        yield item



















