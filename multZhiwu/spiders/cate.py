# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from multZhiwu.items import CateItem


class CateSpider(scrapy.Spider):
    name = 'cate'
    allowed_domains = ['zhiwuwang.com']
    start_urls = ['http://www.zhiwuwang.com/baike']

    custom_settings = {
        'ITEM_PIPELINES': {
            'multZhiwu.pipelines.CatePipelinePipeline': 500,
        },
    }
    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@id="bk-rmfl"]/div[@class="bk-fl"]/div[@class="bk-rm-fl-nr"]/a')

        items = []
        for site in sites:
            item = CateItem()
            item['title']  =  site.xpath('@title').extract()
            item['name']   =   site.xpath('@title').extract()
            item['link']   =   site.xpath('@href').extract()
            item['img_link'] = site.xpath('img/@src').extract()
            item['cateid'] = site.xpath('@href').extract()
            items.append(item)

        return items

