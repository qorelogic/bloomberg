# bloomberg
Bloomberg crawler


```
==================================================
$ scrapy list

companies
```

```
==================================================
$ scrapy crawl companies

.
.
.

2015-04-05 00:58:32-0300 [companies] DEBUG: Scraped from <200 http://investing.businessweek.com/research/common/symbollookup/symbollookup.asp?letterIn=U>
        {'company': u'Under Armour, Inc.',
         'country': u'United States',
         'industry': u'--',
         'ticker': u'UA:US'}
2015-04-05 00:58:33-0300 [companies] DEBUG: Scraped from <200 http://investing.businessweek.com/research/common/symbollookup/symbollookup.asp?letterIn=N>
        {'company': u'Nanobiotix SA',
         'country': u'France',
         'industry': u'--',
         'ticker': u'NANO:FP'}
2015-04-05 00:58:35-0300 [companies] INFO: Dumping spider stats:
        {'downloader/request_bytes': 16768,
         'downloader/request_count': 40,
         'downloader/request_method_count/GET': 40,
         'downloader/response_bytes': 783309,
         'downloader/response_count': 40,
         'downloader/response_status_count/200': 40,
         'finish_reason': 'shutdown',
         'finish_time': datetime.datetime(2015, 4, 5, 3, 58, 35, 363286),
         'item_scraped_count': 4212,
         'request_depth_max': 2,
         'scheduler/memory_enqueued': 169,
         'start_time': datetime.datetime(2015, 4, 5, 3, 57, 43, 837450)}
2015-04-05 00:58:35-0300 [companies] INFO: Spider closed (shutdown)
2015-04-05 00:58:35-0300 [scrapy] INFO: Dumping global stats:
        {'memusage/max': 33587200, 'memusage/startup': 33587200}
```
==================================================
