import scrapy

class AuthorSpider(scrapy.Spider):
    name = "author"

    start_urls = ["https://quotes.toscrape.com/"]


    def parse(self, response):
        author_page_links = response.xpath("/html//div[@class='quote']/span/a/@href")
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.xpath("//li[@class='next']/a/@href")
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):

        yield {
            "fullname": response.xpath("/html/body/div/div[2]/h3/text()").get(),
            "born_date": response.xpath("/html/body/div/div[2]/p[1]/span[1]/text()").get(),
            "born_location": response.xpath("/html/body/div/div[2]/p[1]/span[2]/text()").get(),
            "description": response.xpath("/html/body/div/div[2]/div/text()").get().strip(),
        }


