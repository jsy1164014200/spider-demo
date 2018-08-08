# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['tencent.com']
    url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):
        item = TencentItem()
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            item['positionName'] = each.xpath('./td[1]/a/text()')[0].extract()
            item['positionLink'] = each.xpath('./td[1]/a/@href')[0].extract()
            # item['positionType'] = each.xpath('./td[2]/text()')[0].extract()
            item['positionNum'] = each.xpath('./td[3]/text()')[0].extract()
            item['positionLocation'] = each.xpath('./td[4]/text()')[0].extract()
            item['publishTime'] = each.xpath('./td[5]/text()')[0].extract()

            yield item

        if self.offset < 3501:
            self.offset += 10
            yield scrapy.Request(self.url+str(self.offset),callback=self.parse)

# 将数据交给管道文件处理 
# yield item
# 将请求重新发送给调度器 入队列，出队列，交给下载器下载
# yield scrapy.Request(url,callback = self.parse)