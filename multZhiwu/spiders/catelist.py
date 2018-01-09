# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider



class CatelistSpider(RedisSpider):
    name = 'catelist'
    allowed_domains = ['zhiwu.com']
    start_urls = ['http://www.zhiwuwang.com/']

    def parse(self, response):
        print(response)
        pass
