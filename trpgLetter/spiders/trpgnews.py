import scrapy
from trpgLetter.items import TrpgLetterItem
import re


# crawl arclightTRPG News
class ArclightSpider(scrapy.Spider):
    article = TrpgLetterItem()
    name = "arcspider"
    allowed_domains = ["r-r.arclight.co.jp/info"]
    start_urls = ['http://r-r.arclight.co.jp/info/']

    def parse(self, response):
        # extract infoPage URL
        urls = response.xpath('//body//div[@id="main"]//h2//a/@href').extract()
        for url in urls:
            yield scrapy.Request(response.urljoin(url), callback=self.parse_topics, dont_filter=True)

    # parse date,title,body and URL
    def parse_topics(self, response):
        # title
        article['url'] = response.url
        article['title'] = response.xpath('//body//h2[@class="entry-title singleTitle"]//a/text()').extract_first()
        yield article

# crawl FEAR NEWS
class FearSpider(scrapy.Spider):
    article = TrpgLetterItem()
    name = "fearspider"
    allowed_domains = ["www.fear.co.jp"]
    start_urls = ['http://www.fear.co.jp/upd.htm']

    def parse(self, response):
        urls = response.xpath('//body//a/@href').extract()
        # innersite change fullpath
        urls = ['http://www.fear.co.jp/' + url if re.match(r'^http\://',url) == None else url for url in urls]
        titles = response.xpath('//body//a/text()').extract()
        for (url,title) in zip(urls,titles):
            article['url'] = url
            article['title'] = title
            yield article


# crawl FEAR System NEWS
class FearSystemSpider(scrapy.Spider):
    article = TrpgLetterItem()
    name = "fearsystemspider"
    allowed_domains = ["www.fear.co.jp"]
    start_urls = ['http://www.fear.co.jp']

    def parse(self, response):
        # url
        urls = response.xpath('/html/body/div[3]/table/tbody/tr[1]/td/table[3]/tbody/tr/td/div/div/center/a/@href').extract()
        # title
        titles = response.xpath('/html/body/div[3]/table/tbody/tr[1]/td/table[3]/tbody/tr/td/div/div//text()').extract()
        # remove empty string
        titles = [x.strip() for x in titles]
        # remove empty list and Store title
        titles = [x for x in titles if x != '']

        for (url,title) in zip(urls,titles):
            article['url'] = url
            article['title'] = title
            yield article

# crawl SaikoroFiction NEWS
class SaikoroFictionSpider(scrapy.Spider):
    article = TrpgLetterItem()
    name = "saificspider"
    allowed_domains = ["www.bouken.jp"]
    start_urls = ['http://www.bouken.jp/pd/sf/index.html']

    def parse(self, response):
        titles = response.xpath('//div[@id="honbun_area"]/div/h3/text()').extract()

        for title in titles:
            article['title'] = title
            # same url
            article['url'] = 'http://www.bouken.jp/pd/sf/index.html'
            yield article


# crawl SNE NEWS
