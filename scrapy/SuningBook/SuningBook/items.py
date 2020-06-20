# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SuningbookItem(scrapy.Item):
    # define the fields for your item here like:
    big_category = scrapy.Field()
    mid_category = scrapy.Field()
    small_category = scrapy.Field()
    book_name = scrapy.Field()
    price = scrapy.Field()
    shop = scrapy.Field()
    comment_count = scrapy.Field()
    author = scrapy.Field()
    publishing_house = scrapy.Field()
    publish_date = scrapy.Field()
    image = scrapy.Field()
