# -*- coding: utf-8 -*-
import scrapy


class DisruptionsSpider(scrapy.Spider):
    """ Scrapy web spider for the PTV service updates page """
    name = 'disruptions_spider'
    allowed_domains = ['ptv_disruptions']
    start_urls = ['https://www.ptv.vic.gov.au/disruptions/']

    def parse(self, response):
        """ Does the work of parsing the disruptions web page """
        # get the last updated response
        last_updated = response.css('div.nsb-retrieval-time p::text').extract_first().replace('Last updated ','')
        # get the metro train service statuses list of objects { service, status }
        metro_train_services = response.css('div#disruptions-list div.titleHolder::text')
        metro_train_statuses = response.css('div#disruptions-list span.bubbleType::text')
        metro_data = []
        for service, status in zip(metro_train_services, metro_train_statuses):
            metro_data.append({'service': service.extract(),'status': status.extract()})
        # yield json
        yield {
            'description': 'PTV status updates and service disruptions',
            'last updated': last_updated,
            'metro': metro_data
        }
