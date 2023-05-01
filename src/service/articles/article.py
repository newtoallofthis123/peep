from .spider import *

from scrapy.crawler import CrawlerProcess

class Article:
    def __init__(self, url):
        self.url = url

    def download(self):
        urls = [self.url]
        process = CrawlerProcess(settings={
            'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        process.crawl(MySpider, start_urls=urls)
        process.start()

    def read(self):
        import os
        filename = f"{self.url.split('/')[-1]}.html"
        filename = dir_make(filename)
        if os.path.exists(dir_make(filename)):
            if platform() == "unix":
                os.system(f"xdg-open {filename}")
            elif platform() == "win":
                os.system(f"start {filename}")
            else:
                c_print("Sorry, your platform is not supported", code="danger")
        else:
            c_print("File not found, please download it first", code="danger")

    def all(self):
        import os
        c_print("Here are all the articles you have downloaded:", code="info")
        for file in os.listdir(dir_make("")):
            if file.endswith(".html"):
                c_print(f"{file}", code="info")
            else:
                continue