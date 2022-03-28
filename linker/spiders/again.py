import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LinkerItem


class AgainSpider(CrawlSpider):
    name = 'again'
    allowed_domains = ['wallhaven.cc']
    start_urls = ['https://wallhaven.cc/toplist']

    rules = (
        Rule(LinkExtractor(allow=r''),
             callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        a_list = response.xpath('//section/ul/li')

        for i in a_list:
            # 获取第一页的要点击的 a 链接
            a_href = i.xpath('.//a/@href').extract_first()
            data_src = i.xpath('.//img/@data-src').extract_first()
            yield scrapy.Request(url=a_href, callback=self.nextpage, meta={'data_src': data_src})

    def nextpage(self, response):
        img_url = response.xpath('//div[@class="scrollbox"]//img/@src').extract_first()
        # 接收参数
        data_src = response.meta['data_src']
        src = LinkerItem(src=img_url, data_src=data_src)
        print(src)
        yield src
