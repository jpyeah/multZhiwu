# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item , Field


class MultzhiwuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CateItem(Item):

    name = Field()
    cateid = Field()
    title  = Field()
    link   = Field()
    img_link = Field()

class CateListItem(Item):

    name = Field()
    cateid = Field()
    title  = Field()
    parentid  = Field()