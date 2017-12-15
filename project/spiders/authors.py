import scrapy

class Authors(scrapy.Spider):
    name = "author"
    start_urls = ['http://quotes.toscrape.com/',]
    def parse(self, response):

        for authorhref in response.css('.author + a::attr(href)'):
            yield response.follow(authorhref, self.parse_author) 

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href,self.parse)
        pass

    def parse_author(self,response):

        def utilfun(query):
            return response.css(query).extract_first().strip()

        yield {
            'name': utilfun('h3.author-title::text'),
            'born': utilfun('.author-born-date::text'),
            'desc': utilfun('.author-description::text'),
        }
        pass