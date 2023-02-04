class YTSpider:
    def __init__(self, url):
        self.url = url

    def video_info_spider(self):
        import youtube_dl
        url = self.url
        options = {"no_warnings": True, "quiet": True}
        with youtube_dl.YoutubeDL(options) as ytdl:
            video_info = ytdl.extract_info(url, download=False)
            video_url_stream = [video_info["formats"][-1]["url"], video_info["formats"][-2]["url"],
                                video_info["formats"][-3]["url"]]
            audio_url_stream = [video_info["requested_formats"][1]["url"], video_info["formats"][1]["url"]]
            video_thumnail = video_info['thumbnails'][-1]['url']
            return {
                "url_stream": video_url_stream,
                "audio_stream": audio_url_stream,
                "title": video_info["title"],
                "description": ' '.join(video_info["description"].split("\n")),
                "thumbnail": video_thumnail
            }

    def video_dl(self):
        import youtube_dl
        options = {"no_warnings": True, "quiet": True}
        with youtube_dl.YoutubeDL(options) as ytdl:
            ytdl.download([self.url])

    def audio_dl(self):
        import youtube_dl
        options = {"no_warnings": True, "quiet": True, "format": "bestaudio"}
        with youtube_dl.YoutubeDL(options) as ytdl:
            ytdl.download([self.url])