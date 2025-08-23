# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FilePipeline:
    def open_spider(self,spider):
        print('ok3')
        self.f = open('file.jsonl',mode='w',encoding='utf-8')
    def close_spider(self,spider):
        self.f.close()
        print('ok2')
    def process_item(self, item, spider):
        self.f.write(f"{item['page']}\n")
        print('ok')




