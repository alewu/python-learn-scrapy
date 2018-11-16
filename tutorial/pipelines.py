# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tutorial.items import TutorialItem


class TutorialPipeline(object):
    def __init__(self):
        self.file = open(file='test1.html', mode='w', encoding='utf-8')

    def process_item(self, item, spider):
        for i in item['url']:
            text = '<img src="' + i + '" alt = "" />' + "\n"
            self.file.writelines(text)

    def close_spider(self, spider):
        self.file.close()
