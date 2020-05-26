# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem

class PersonalemailSpider(XMLFeedSpider):
    name = 'personalemail'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/test.xml']
    iterator = 'iternodes' # 迭代器
    itertag = 'person' # 用来设置开始迭代的节点

    def parse_node(self, response, selector):
        #方法在节点与所提供的标 签名相符合的时候会被调用，在该方法中，可以进行一些信息的提取 和处理的操作
        item =MyxmlItem()
        item['link'] = selector.xpath("/person/email/text()").extract()
        print(item['link'])
