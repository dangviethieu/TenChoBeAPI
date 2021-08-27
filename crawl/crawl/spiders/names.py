from scrapy import Spider, Request
from scrapy.loader import ItemLoader
from ..items import NameItem
import logging


class ExtractNameSpider(Spider):
    name = 'names'
    allowed_domains = ['tenchocon.vn']
    start_urls = ['https://tenchocon.vn']

    def __init__(self):
        logger = logging.getLogger('scrapy.middleware')
        logger.setLevel(logging.WARNING)
        self.html_file = open("tenchobe.html", 'w')
        self.index = 0

    def parse(self, response):
        # self.html_file.write(response.text)
        # self.html_file.close()
        for name_selector in response.xpath('//table[@id="ContentPlaceHolderTenChCon_DataList1"]//td/a'):
            name = name_selector.xpath('.//text()').get()
        #     item = ItemLoader(item=NameItem(), selector=name_selector)
            # item.add_xpath('sex', '@class')
            # item.add_xpath('description', '@href')
            sex = name_selector.xpath('.//@class').get()
            yield {
                "name": name.replace('\r', '').replace('\n', '').replace('\t', '').strip(),
                "sex": sex,
            }
        self.index += 1
        if self.index < 14:
            new_page_url = f"https://tenchocon.vn/?ho=&name=&sex=0&page={self.index}"
            new_page = response.urljoin(new_page_url)
            self.logger.info('Page scraped, clicking on "more"! new_page = {}'.format(new_page))
            yield Request(new_page, callback=self.parse)

