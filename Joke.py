import scrapy

class Joke(scrapy.Spider):
    name = "blogSpider"
    start_urls = ["http://quotes.toscrape.com/tag/humor/"]
    
    def parse(self, response):
        for joke in response.xpath("//div[@class=\"quote\"]"):
            print(joke.xpath("span[1]/text()").extract())
            print(joke.xpath("span[2]/small/text()").extract())
            yield{"content":joke.xpath("span[1]/text()").extract(),
                  "author":joke.xpath("span[2]/small/text()").extract()} 
             
        next_page = response.xpath("//li[@class=\"next\"]/a/@href").extract()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse())