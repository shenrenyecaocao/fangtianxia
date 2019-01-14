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

    def process_item(self, item, spider):
        print json.dumps(dict(item), encoding='UTF-8', ensure_ascii=False)
        self.f.write(json.dumps(dict(item)) + "\n")
        return item

    def close_spider(self, spider):
        self.f.close()
