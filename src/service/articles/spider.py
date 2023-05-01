import scrapy
from ..format import *
from ..brain import *


def dir_make(file):
    import os
    home_dir = os.path.expanduser('~')
    os.mkdir(os.path.join(home_dir, ".peep")) if not os.path.exists(
        os.path.join(home_dir, ".peep")) else None
    os.mkdir(os.path.join(home_dir, ".peep", "articles")) if not os.path.exists(
        os.path.join(home_dir, ".peep", "articles")) else None
    return os.path.join(home_dir, ".peep", "articles", file)

class MySpider(scrapy.Spider):
    name = 'myspider'

    def __init__(self, start_urls=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = start_urls or []

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extract data from the response using Scrapy selectors
        title = response.css('title::text').get()
        html = response.body.decode('utf-8')
        filename = f"{response.url.split('/')[-1]}.html"
        if(os.path.exists(dir_make(filename))):
            c_print("File already exists", code="warning")
            return
        with open(dir_make(filename), 'w', encoding='utf-8') as f:
            html = f'<p>Downloaded at {response.url}</p>' + html
            f.write(html)
        c_print(f"Downloaded {title} at {filename}", code="success")
        open_choice = ask("Do you want to open the file?")
        if open_choice:
            if platform() == "unix":
                os.system(f"xdg-open {filename}")
            elif platform() == "win":
                os.system(f"start {filename}")
        else:
            c_print("Okay...", code="info")
        yield {'title': title}