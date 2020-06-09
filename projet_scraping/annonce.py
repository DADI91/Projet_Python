import requests
import scrapy


class BlogSpider(scrapy.Spider):
    
    name = 'blogspider'
    start_urls = ['https://www.seloger.com']

    def parse(self, response):
        for title in response.css('div.ContentZone__Title-wghbmy-7'):
            yield {'charactere': title.css('div ::attr(href)').get()}

"""
name = 'seloger'
    url = "https://www.seloger.com/list.htm?projects=2%2C5&types=2&natures=1%2C2%2C4&isochronepoints=%5B%7B%22id%22%3A0%2C%22point%22%3A%7B%22lat%22%3A48.266549%2C%22lng%22%3A3.255339%2C%22mode%22%3A%7B%22type%22%3A%22Car%22%2C%22place%22%3A0%2C%22options%22%3A%7B%22rushHour%22%3Atrue%7D%7D%7D%2C%22timeRange%22%3A%5B1800%5D%7D%5D&price=NaN%2F230000&enterprise=0&qsVersion=1.0&LISTING-LISTpg="

    def get_pages(url, nb):
        pages = []
        for i in range(1, nb+1):
            j = url + str(i)
            pages.append(j)
        return pages
    pages = get_pages(url, 2)
"""