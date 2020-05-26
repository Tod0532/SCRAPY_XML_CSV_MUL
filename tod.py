# -*- coding: utf-8 -*-
import scrapy


class TodSpider(scrapy.Spider):
    name = 'tod'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
