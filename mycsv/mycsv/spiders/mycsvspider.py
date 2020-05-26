# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from mycsv.items import MycsvItem

class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['iqianyue.com']
    print("-----------------")
    start_urls = ['http://yum.iqianyue.com/mydata.csv']
    #定义heders
    headers = [ 'name', 'sex', 'addr','email']
    #定义间隔符
    delimiter = ','
    def parse_row(self, response, row):
        print("----------------e-")
        i = MycsvItem
        i['name'] = row['name'].encode()
        i['sex'] = row['sex'].encode()
        i['addr']=row['addr'].encode()
        i['email']=row['email'].encode()
        print(i['name'])
        print(i['sex'])
        print(i['addr'])
        print(i['email'])
        print("-----------------")
        return i
