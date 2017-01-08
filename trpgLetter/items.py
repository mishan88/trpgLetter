import scrapy

class TrpgLetterItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
