# encoding:utf-8
import scrapy
from scrapy.http import Request
from fangtianxia.items import FangtianxiaItem
from scrapy.selector import Selector


class FangTianXiaSpider(scrapy.Spider):
    name = "fangtianxia"
    # allowed_domains = ["xian.esf.fang.com"]
    start_urls = [
        "https://xian.esf.fang.com/housing/"
    ]

    def parse(self, response):
        url_list = response.xpath('//div[@class="houseList"]//a[@class="plotTit"]/@href').extract()
        url_list = map(lambda url: "https:{}xiangqing/".format(url), url_list)
        print url_list
        for url in url_list[:1]:
            yield Request(url, callback=self.parse_info)

        # next_url = response.xpath('//a[@id="PageControl1_hlk_next"]/@href').extract_first()
        # if next_url is not None:
        #     next_url = "https://xian.esf.fang.com{}".format(next_url)
        #     yield scrapy.Request(next_url, callback=self.parse)

    def parse_info(self, response):
        item = FangtianxiaItem()
        item['house_name'] = response.xpath('//div[@class="logoBox_sq"]//a[@class="tt"]/text()').extract_first()
        sel = Selector(response)
        _dd = sel.xpath('//div[@class="box"]/div[@class="inforwrap clearfix"]/dl[@class=" clearfix mr30"]/dd')
        # pprint(_dd)
        # 小区地址
        # 物业公司
        # 业办公地点
        # 物业办公电话
        for d in _dd:
            k = d.xpath('strong/text()').extract_first()
            v = d.xpath('text()').extract_first()
            try:
                k = k.encode('gbk')
            except Exception as e:
                k = k.encode('utf-8')
                print e
            print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
            print k
            print type(k)
            print '小区地址'
            print type('小区地址')
            print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
            if '小区地址' in k:
                item['house_address'] = v
            else:
                item['house_address'] = ''
            if '物业公司' in k:
                item['property_name'] = v
            else:
                item['property_name'] = ''
            if '业办公地点' in k:
                item['property_address'] = v
            else:
                item['property_address'] = ''
            if '物业办公电话' in k:
                item['property_tel'] = v
            else:
                item['property_tel'] = ''
        yield item