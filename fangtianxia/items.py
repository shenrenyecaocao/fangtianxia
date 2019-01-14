# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangtianxiaItem(scrapy.Item):
    # define the fields for your item here like:
    house_name = scrapy.Field()
    house_address = scrapy.Field()
    property_name = scrapy.Field()
    property_address = scrapy.Field()
    property_tel = scrapy.Field()
