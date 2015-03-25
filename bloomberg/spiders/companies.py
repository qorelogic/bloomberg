
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from bloomberg.items import BloombergItem

class CompaniesSpider(CrawlSpider):
    
    name = "companies"
    allowed_domains = ["investing.businessweek.com"]
    start_urls = (
        'http://investing.businessweek.com/research/common/symbollookup/symbollookup.asp?letterIn=A',
    )
    
    rules = ( 
        #Rule(SgmlLinkExtractor(allow=r'symbollookup/symbollookup.asp\?letterIn=[A]'), callback='parse_item', follow = True),
        Rule(SgmlLinkExtractor(allow=r'symbollookup/symbollookup.asp\?letterIn=[A-B]&firstrow=[0-9]'), callback='parse_item', follow = True),
    )

    # scrapy parse --spider=companies -c parse 'http://investing.businessweek.com/research/common/symbollookup/symbollookup.asp?letterIn=A'
    def parse_item(self, response):
        
        hxs = HtmlXPathSelector(response)
        items = []
        company_names = hxs.select('//*[@id="columnLeft"]/table/tbody/tr/td[1]/a/text()').extract()
        country_names = hxs.select('//*[@id="columnLeft"]/table/tbody/tr/td[2]/text()').extract()
        industry_names = hxs.select('//*[@id="columnLeft"]/table/tbody/tr/td[3]/text()').extract()
        ticker = hxs.select('//*[@id="columnLeft"]/table/tbody/tr/td[1]/a/@href').extract()

        for com, count, ind, tik in zip(company_names, country_names, industry_names, ticker):
            tik = tik.split('=')[1]
            #print [com, count, ind, tik]
            items.append(BloombergItem(company=com, country=count, industry=ind, ticker=tik))
            #di = {'company':com, 'country':count, 'industry':ind, 'ticker':tik}; items.append(di)
            #print di
        return items
        