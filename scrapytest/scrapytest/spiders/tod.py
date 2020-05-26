# -*- coding: utf-8 -*-
import scrapy
from scrapytest.items import ScrapytestItem

class TodSpider(scrapy.Spider):
    name = 'tod'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://slide.news.sina.com.cn/s/slide_1_2841_103185.html',
                  'http://slide.mil.news.sina.com.cn/k/slide_8_193_45192.html#p=1',
                  'http://news.sina.com.cn/pl/2016-09-12/doc-ifxvukhv8147404.shtml',]

    def parse(self, response):
        item=ScrapytestItem()
        item["urlname"]=response.xpath("/html/head/title/text()")
        print(item["urlname"])
    #重新初始化方法__init__(),并设置参数myurl
    #args 是 arguments 的缩写，表示位置参数；kwargs 是 keyword arguments 的缩写，表示关键字参数。
    def __init__(self,myurl=None,*args,**kwargs):
        super(TodSpider,self).__init__(*args,**kwargs)
        print("要爬取的网址为： %s"%myurl)
        self.start_urls=["%s"%myurl]


