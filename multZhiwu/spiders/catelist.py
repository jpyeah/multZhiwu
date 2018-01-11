# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider



class CatelistSpider(RedisSpider):
    name = 'catelist'
   # allowed_domains = ['zhiwu.com']
   # start_urls = ['http://www.zhiwuwang.com/']
    redis_key ='catelist:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(CatelistSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        title = response.css('title::text').extract_first()

        print(title)
        pass
