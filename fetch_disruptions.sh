rm ~/ptv_disruptions.json 2> /dev/null
scrapy crawl disruptions_spider -o ~/ptv_disruptions.json
