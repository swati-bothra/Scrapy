import scrapy

class QuoteSpider(scrapy.Spider):
	name = "quotes"
	#def start_requests(self):
		#urls=['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/',]
		#for url in urls:
		#	yield scrapy.Request(url=url, callback=self.parse)
		#	pass
		#pass
	start_urls =['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/',]

	def parse(self, response):
		#pageno = response.url.split('/')[-2]
		#filename = "quotes_%s" % pageno
		#with open(filename, 'wb') as f:
		#	f.write(response.body)

		for quote in response.css('div.quote'):
			yield {
				'title' : quote.css('span.text::text').extract_first(),
				'author' : quote.css('small.author::text').extract_first(),
				'tags' : quote.css('div.tags a.tag::text').extract(),
			}

		#next_page = response.css('li.next a::attr(href)').extract_first().encode('ascii')
		#if next_page is not None:
			#1#next_page = response.urljoin(next_page)
			#1#yield scrapy.Request(next_page, callback=self.parse)
			#2#yield response.follow(next_page,callback=self.parse) 
		
		#for href in response.css('li.next a::attr(href)'):
		#	yield response.follow(href,callback=self.parse)

		for a in response.css('li.next a'):
			yield response.follow(a,callback=self.parse)

		pass
	
