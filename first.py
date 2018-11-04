import scrapy

class BlogSpider(scrapy.Spider):
    name = 'quotes_spider'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # Creating a parser for each quote
        
        for quote in response.css('div.quote'):
            yield {'author': quote.css('small.author::text').extract_first()}
            yield {'quote': quote.css('span.text::text').extract_first()}
            yield {'tag': quote.css('a.tag::text').extract()}
