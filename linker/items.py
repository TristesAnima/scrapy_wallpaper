# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LinkerItem(scrapy.Item):
    # define the fields for your item here like:
    data_src = scrapy.Field()
    src = scrapy.Field()
