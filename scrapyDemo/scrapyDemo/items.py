# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 这是一个 类字典 model数据
class ItcastItem(scrapy.Item):
    name = scrapy.Field()# 名字
    title = scrapy.Field()# 职称
    info = scrapy.Field()# 个人简介
