import scrapy
from scrapyDemo.items import ItcastItem

# 创建一个爬虫类
class ItcastSpider(scrapy.Spider):
    name = "itcast"
    # 允许爬虫的作用范围
    allowd_domains = ["http://www.itcast.cn/"]
    # 爬虫起司的url
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    def parse(self,response):
        # response 就是一个lxml对象Selector
    
        for each in response.xpath('//div[@class="li_txt"]'):
            item = ItcastItem()
            # name  
            name = each.xpath('./h3/text()')[0].extract() #extract()将对象弄成str
            # title
            title = each.xpath('./h4/text()')[0].extract()
            # info
            info = each.xpath('./p/text()')[0].extract()
            item['name'] = name
            item['title'] = title
            item['info'] = info

            yield item  #常用生成器


