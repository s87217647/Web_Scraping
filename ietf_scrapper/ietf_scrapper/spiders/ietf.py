import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscrapping.com']
    start_urls = ['https://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        title = response.xpath('//span[@®®class="title"]/text()').get()
        author_name = response.xpath('//span[@class="author-name"]/text()').get()
        date = response.xpath('//span[@class="date"]/text()').get()
        text = response.xpath('//span[@class="text"]/text()').get()



        #challenge
        # Author name
        # Title
        # Date
        # text
        # return {"title" : title}
        # return {"author_name" : author_name}

        return{"title": title, "author name": author_name, "date" : date, "text" : text }