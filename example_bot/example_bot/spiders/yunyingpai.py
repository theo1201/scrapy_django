

from example_bot.items import YunyingItem
import scrapy

class  YunyingpaiSpider(scrapy.Spider):
    name = 'yunyingpai'
    allowed_domains = ['yunyingpai.com']
    start_urls = ['https://www.yunyingpai.com/user/page/' + str(i) for i in range(1, 2)]

    def parse(self, response):
        urls = response.xpath("//div/section//h3/a/@href").extract()
        for i in urls:
            yield scrapy.Request(i, callback=self.parse2)

    def parse2(self, response):
        items = YunyingItem()

        items["title"] = response.xpath("//div/article/header/h2/text()").extract_first()
        items["content"] = response.xpath("//div/article/div[4]").xpath("string(.)").extract_first().strip()
        items["link"] = response.url
        items["editor"] = response.xpath('//div/article/header/div/a/text()').extract_first()
        items["publishtime"] = response.xpath("//div/article/header/div/time/text()").extract_first()

        yield items
