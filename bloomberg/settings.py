# Scrapy settings for bloomberg project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'bloomberg'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['bloomberg.spiders']
NEWSPIDER_MODULE = 'bloomberg.spiders'
ITEM_PIPELINES = {
    'bloomberg.pipelines.JsonWithEncodingPipeline': 300,
    #'bloomberg.pipelines.PrintPipeline': 300,
    'bloomberg.pipelines.XmlExportPipeline': 300,
}
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

