# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy              # 导入scrapy
from scrapy.item import Field    # 从scrapy.item中导入Field模块


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(scrapy.Item):   # 定义Item, 获取从网站所需的条目, 如标题, 网站链接, 详细描述
    title = Field()
    link = Field()
    desc = Field()
