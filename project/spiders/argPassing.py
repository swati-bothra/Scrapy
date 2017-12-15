import scrapy

class Args(scrapy.Spider):
	name = 'args'
	def start_requests(self):
		url = 'http://quotes.toscrape.com/'
		tag = getattr(self,'tag',None)
		if tag is not None:
			url = url + 'tag/' + tag
		yield scrapy.Request(url,self.parse)
		pass

	def parse(self,response):
		for quote in response.css('div.quote'):
			yield {
				'title' : quote.css('span.text::text').extract_first(),
				'author' : quote.css('small.author::text').extract_first(),
			}

		next_page = response.css('li.next a::attr(href)').extract_first().encode('ascii')
		if next_page is not None:
			yield response.follow(next_page,self.parse) 
		pass
	