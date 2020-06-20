# -*- coding: utf-8 -*-
import scrapy
from SuningBook.items import SuningbookItem
from copy import deepcopy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['book.suning.com', 'list.suning.com',
                       'product.suning.com', 'imgservice.suning.cn']
    start_urls = ['http://book.suning.com/']

    def parse(self, response):
        # 获取大类div列表
        big_div_list = response.xpath('//div[@class="menu-item"]')
        # 循环大类
        for big_div in big_div_list:
            # 初始化item
            item = SuningbookItem()
            # 获取大类的名字
            item['big_category'] = big_div.xpath('.//dt//a/text()').extract_first()
            # 获取中类的a列表
            mid_a_list = big_div.xpath('.//dd//a')
            # 循环中类a列表
            for mid_a in mid_a_list:
                # 获取中类的名字
                item['mid_category'] = mid_a.xpath('./text()').extract_first()
                # 获取中类的url
                mid_url = mid_a.xpath('./@href').extract_first()
                yield scrapy.Request(
                    mid_url,
                    callback=self.parse_list,
                    meta={'item': deepcopy(item)}
                )

    def parse_list(self, response):
        # 接收item
        item = deepcopy(response.meta['item'])
        # 获取书籍li列表
        book_li_list = response.xpath('//ul[@class="clearfix"]/li')
        # 循环书籍li
        for book_li in book_li_list:
            book_url = 'http:' + book_li_list.xpath('.//a[@class="sellPoint"]/@href').extract_first()
            yield scrapy.Request(
                book_url,
                callback=self.parse_detail,
                meta={'item': deepcopy(item)}
            )
        # 获取下一页url
        next_url = response.xpath('//a[@id="nextPage"]/@href').extract_first()
        if next_url:
            next_url = 'https://list.suning.com/' + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse_list,
                meta={"item":response.meta["item"]}
            )

    def parse_detail(self, response):
        # 接收item
        item = deepcopy(response.meta['item'])
        # 获取书名
        item['book_name'] = response.xpath('//h1[@id="itemDisplayName"]/text()').extract()
        item['book_name'] = ''.join([i.strip() for i in item['book_name']])
        # 获取商家名
        item['shop'] = response.xpath('//div[@class="si-intro-list"]/dl[1]/dd/a/text()').extract_first()
        # 获取作者
        item['author'] = response.xpath('//ul[@class="bookcon-param clearfix"]/li[1]/span/text()').extract()
        item['author'] = ''.join(item['author'])
        # 获取出版社
        item['publishing_house'] = response.xpath('//li[@class="pb-item"][2]/text()').extract_first().strip()
        # 获取出版日期
        item['publish_date'] = response.xpath('//li[@class="pb-item"][3]/span[2]/text()').extract_first()
        # 获取图片
        item['image'] = response.xpath('//div[@class="imgzoom-main"]/a[@id="bigImg"]/img/@src').extract_first()
        yield item
