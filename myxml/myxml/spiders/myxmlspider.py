# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem

class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    # start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    start_urls = ['http://blog.sina.com.cn/rss/1812671331.xml']
    iterator = 'iternodes' # 迭代器
    itertag = 'rss' # 用来设置开始迭代的节点

    def parse_node(self, response, selector):
        #方法在节点与所提供的标 签名相符合的时候会被调用，在该方法中，可以进行一些信息的提取 和处理的操作
        item =MyxmlItem()
        item['title']=selector.xpath("/rss/channel/item/title/text()").extract()
        item['link'] = selector.xpath("/rss/channel/item/link/text()").extract()
        item['author'] = selector.xpath("/rss/channel/item/author/text()").extract()

        for j in range(len(item['author'])):
            print("第"+str(j+1)+"篇文章")
            print("标题是： ")
            print(item['title'][j])
            print("对应链接是：")
            print(item['link'][j])
            print("对应作者是： ")
            print(item['author'][j])
        return item
