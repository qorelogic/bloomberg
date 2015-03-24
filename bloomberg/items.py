# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class BloombergItem(Item):
    # define the fields for your item here like:
    company = Field()
    country = Field()
    industry = Field()
    ticker = Field()
    pass
