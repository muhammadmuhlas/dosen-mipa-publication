# Author: Muhammad Muhlas <muhammadmuhlas3@gmail.com>
import scrapy
import json
import os
import scholar

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://dcse.fmipa.ugm.ac.id/site/en/profil-pengajar/']

    def parse(self, response):
        table = response.xpath('//*[@class="post-content"]//table//tbody')
        rows = table.xpath('//tr')
        total = len(rows)

        for i in range(total):
            if i == 0 or i == total-1:
                print('skipped: unusable html')
            else:
                print(i)
                name = rows[i].xpath('td//div//text()')[1].extract()
                url = rows[i].xpath('td//div//a/@href').extract()
                tags = rows[i].xpath('td//ul//li//div//text()').extract()
                print(name)
                print(url)
                print(tags)
                querier = scholar.ScholarQuerier()
                settings = scholar.ScholarSettings()

                querier.apply_settings(settings)
                query = scholar.SearchScholarQuery()
                query.set_words(name)

                querier.send_query(query)
                scholar.txt(querier, with_globals=1)
