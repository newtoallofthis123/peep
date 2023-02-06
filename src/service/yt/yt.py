import os

from youtube_search import YoutubeSearch
from youtubesearchpython import CustomSearch, VideoSortOrder, ChannelsSearch, Search, Video
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
from ..format import *

class Yt:
    def __init__(self, query):
        self.query = query

    def print_results(self):
        search_term = self.query
        Console().print("Search Results powered by [link=https://github.com/newtoallofthis123/ytps]ytps[/link]")
        table = Table(title=Panel(f'Results for [red]{search_term.capitalize()}'), show_header=True,
                      header_style="bold green")
        table.add_column("Released", style="dim", width=20)
        table.add_column("Title", style="yellow")
        table.add_column("Channel", style="cyan")
        table.add_column("Url", no_wrap=True, style="blue")

        results = YoutubeSearch(search_term, max_results=20).to_dict()
        for i in results:
            video_url_for_table = f'https://youtu.be/{i["id"]}'
            channel = i["channel"]
            channelsSearch = ChannelsSearch(channel, limit=10, region='US')
            channelsSearch_content = channelsSearch.result()
            table.add_row(
                i["publish_time"],
                i["title"],
                f'[link={channelsSearch_content["result"][0]["link"]}]{channel}[/link]',
                video_url_for_table,
            )
        table.caption = ":zap: Made by [link=https://newtoallofthis123.github.io/About]NoobScience[/link]"
        Console().print(table)
    def search(self):
        from random import choice
        spinners = ["clock", "monkey", "point", "dots8"]
        with Console().status("Getting Results from [link=https://yt.be]YouTube[/link]. This might take a while...\n", spinner=choice(spinners)):
            self.print_results()

    def get_video(self):
        video_url = self.query
        video_info = Video.getInfo(video_url)
        c_print(f"Getting Video Info for {video_url}...", code="info")
        Console().print(Panel(
            f'[cyan]{video_info["title"]}[/]\n\n[green bold]Url: [/]{video_info["link"]}\n[green bold]View Count: [/]{video_info["viewCount"]["text"]}\n[green bold]Channel: [/]{video_info["channel"]["name"]}\n[green bold]Channel Link: [/]{video_info["channel"]["link"]}'),
                      justify="center")
        from .spider import YTSpider
        spider = YTSpider(video_url)
        video = spider.video_info_spider()
        # Console().print(video)
        play_response = ask("Do you want to play this video?")
        if play_response:
            from .ui import Ui
            ui = Ui(video["url_stream"][0], video)
            c_print("Starting Server...", code="info")
            import webbrowser
            webbrowser.open("http://localhost:5000")
            c_print("Server Started!&&Opening Browser", code="success")
            ui.server()

    def dl_video(self):
        video_url = self.query
        c_print("Getting Video Info...", code="info")
        video_info = Video.getInfo(video_url)
        dl_response = ask("Do you want to download this video?")
        if dl_response:
            Console().print(Panel(f'Downloading {video_info["title"]}'))
            from .spider import YTSpider
            spider = YTSpider(video_url)
            from random import choice
            spinners = ["clock", "monkey", "point", "dots8"]
            with Console().status(
                    "Getting Results from [link=https://yt.be]YouTube[/link]. This might take a while...\n",
                    spinner=choice(spinners)):
                spider.video_dl()

    def dl_audio(self):
        search_term = self.query
        results = YoutubeSearch(search_term, max_results=20).to_dict()
        video_url = f'https://youtu.be/{results[0]["id"]}'
        video_response = ask("Do you want to download this video?")
        if video_response:
            Console().print(Panel(f'Downloading {results[0]["title"]}'))
            from .spider import YTSpider
            spider = YTSpider(video_url)
            from random import choice
            spinners = ["clock", "monkey", "point", "dots8"]
            with Console().status(
                    "Getting Results from [link=https://yt.be]YouTube[/link]. This might take a while...\n",
                    spinner=choice(spinners)):
                spider.audio_dl()

    def stream_audio(self):
        search_term = self.query
        results = YoutubeSearch(search_term, max_results=20).to_dict()
        video_url = f'https://youtu.be/{results[0]["id"]}'
        # video_response:
        Console().print(Panel(f'Streaming {results[0]["title"]}'))
        from .spider import YTSpider
        spider = YTSpider(video_url)
        from random import choice
        spinners = ["clock", "monkey", "point", "dots8"]
        with Console().status(
                "Getting Results from [link=https://yt.be]YouTube[/link]. This might take a while...\n",
                spinner=choice(spinners)):
            video = spider.video_info_spider()
        from .ui import Ui
        ui = Ui(video["audio_stream"][0], video)
        c_print("Starting Server...", code="info")
        import webbrowser
        webbrowser.open("http://localhost:5000")
        c_print("Server Started!&&Opening Browser", code="success")
        ui.audio_server()

    def stream_video(self):
        search_term = self.query
        results = YoutubeSearch(search_term, max_results=20).to_dict()
        video_url = f'https://youtu.be/{results[0]["id"]}'
        # video_response:
        Console().print(Panel(f'Streaming {results[0]["title"]}'))
        private_response = ask(
            "Do you want to play this video privately or on youtube.com?")
        if private_response:
            from .spider import YTSpider
            spider = YTSpider(video_url)
            from random import choice
            spinners = ["clock", "monkey", "point", "dots8"]
            with Console().status(
                    "Getting Results from [link=https://yt.be]YouTube[/link]. This might take a while...\n",
                    spinner=choice(spinners)):
                video = spider.video_info_spider()
            from .ui import Ui
            ui = Ui(video["url_stream"], video)
            c_print("Starting Server...", code="info")
            import webbrowser
            webbrowser.open("http://localhost:5000")
            c_print("Server Started!&&Opening Browser", code="success")
            ui.server()
        else:
            import webbrowser
            c_print(f"Opening {results[0]['title']} in your default webbrowser...", code="info")
            webbrowser.open(
                "https://youtu.be/" + results[0]["id"] + "?autoplay=1")
