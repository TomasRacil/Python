import scrapy
import codecs
import re
import json
from ..items import WebcrawlerItem

def unmangle_utf8(match):
    escaped = match.group(0)                   # '\\u00e2\\u0082\\u00ac'
    hexstr = escaped.replace(r'\u00', '')      # 'e282ac'
    buffer = codecs.decode(hexstr, "hex")      # b'\xe2\x82\xac'

    try:
        return buffer.decode('utf8')           # '€'
    except UnicodeDecodeError:
        print("Could not decode buffer: %s" % buffer)




class Spider(scrapy.Spider):
    name = "alzaSpidey"

    start_urls = [
        'https://www.alza.cz/akcni-zbozi'
    ]

    def parse(self, response):

        items = WebcrawlerItem()

        all_boxes = response.css('div.browsingitem')

        for box in all_boxes:

            item = box.css('a.name::text').extract()
            price = box.css('span.c2::text').extract()
            priceBefore = box.css('span.np2::text').extract()
            discount = box.css('span.np::text').extract()

            items['item'] = item
            items['price'] = price
            items['priceBefore'] = priceBefore
            items['discount'] = discount

            yield items

        next_page = response.css('a.next::attr(href)').get()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)