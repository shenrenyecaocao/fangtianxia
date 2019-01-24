# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json

class FangtianxiaPipeline(object):
    def open_spider(self, spider):
        filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', "house.json")
        self.f = open(filepath, "w")
        self.f.write("[\n")

    def process_item(self, item, spider):
        data = dict(item)
        print "$$$$$$$$$$$$$$$$$$$4"
        print data
        print "$$$$$$$$$$$$$$$$$$$4"

        house_name = data.get('house_name', '')
        house_address = data.get('house_address', '')
        property_name = data.get('property_name', '')
        property_address = data.get('property_address', '')
        property_tel = data.get('property_tel', '')
        info = '{"house_name": "%s", "house_address": "%s", "property_name": "%s", "property_address": "%s", "property_tel": "%s"},\n' % (house_name, house_address, property_name, property_address, property_tel)
        self.f.write(info + "\n")
        return item

    def close_spider(self, spider):
        self.f.write("]\n")
        self.f.close()