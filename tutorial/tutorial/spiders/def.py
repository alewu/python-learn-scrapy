# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tutorial.items import TutorialItem


class DefSpider(CrawlSpider):
    name = 'def'
    allowed_domains = ['ww.vrzhiyuan8.com']
    start_urls = ['http://ww.vrzhiyuan8.com/']

    links = LinkExtractor(allow='http://ww.vrzhiyuan8.com/\d+.html')
    rules = (
        Rule(links, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        url_item = TutorialItem()
        for img in response.xpath('//*[@id="post_content"]/p/a/img'):
            url_item['url'] = img.xpath('.//@src').extract()
            yield url_item
