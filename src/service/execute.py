from .brain import *
from urllib.parse import quote
from .format import *
import webbrowser

class Execute:
    def __init__(self, action, query):
        self.action = action
        self.query = query
    def search(self):
        engine = self.action
        query = self.query
        engines = get_ops()["engines"]
        if engine not in engines:
            engine = "google"
            engine_response = ask(f"Search engine not specified, peep wants to use {engine}. Do we continue?")
            if engine_response:
                c_print(f"Continuing with {engine}...", code="success")
            else:
                engine = prompt("Enter the search engine")
                if engine in engines:
                    c_print(f"Continuing with {engine}...", code="success")
                else:
                    c_print(f"Search engine {engine} not supported", code="danger")
                    c_print("Continuing with default...", code="danger")
                    engine = "google"
            query = self.action + " " + self.query
        if engine in engines:
            search_query = f'{engines[engine]}{quote(query)}'
            ask_response = ask(f'Do you want to open {engine} in the web browser?')
            if ask_response:
                webbrowser.open(search_query)
                c_print(f"Opened {engine} in the web browser", code="success")
            else:
                c_print("Not opening query in the web browser...", code="danger")
                copy_res = ask(f'Do you want to copy the url instead?')
                copy(search_query) if copy_res else c_print("Okay...", code="info")
        else:
            c_print(f"No info found on Search Engine : {engine}", code="danger")

    def editor(self):
        from .editor.editor import Editor
        file = self.action
        lang = self.query
        if lang == "":
            file_mapper = get_ops()["file_stuff"]
            lang = file_mapper["." + str(file).split('.')[1]]
            lang_response = ask(f"Language not specified, peep thinks it is {lang} Do we continue?")
            if lang_response:
                c_print(f"Continuing with {lang}...", code="success")
            else:
                lang = prompt("Enter the language: ")
                if lang in file_mapper.values():
                    c_print(f"Continuing with {lang}...", code="success")
                else:
                    c_print(f"Language {lang} not supported", code="danger")
                    c_print("Continuing with default...", code="danger")
                    lang = "text"
        c_print(f"Trying to Open {file} in SnakeRun Editor", code="info")
        editor_instance = Editor(file, lang)
        editor_instance.open()

    def md(self):
        from .editor.editor import Md
        file = self.action
        c_print(f"Trying to Open {file} in SnakeRun + HTMLer Markdown Editor", code="info")
        md_instance = Md(file)
        md_instance.up()

    def ai(self):
        from .ai.key import Key
        key = Key()
        api_key = key.get_key()
        from .ai.ai import Ai
        ai = Ai(api_key)
        ai.ask(self.query)

    def qr(self):
        from .qr.qr import Qr
        qr = Qr(self.action, self.query)
        qr.make()

    def img_qr(self):
        from .qr.qr import Qr
        qr = Qr(self.action, self.query)
        qr.img_qr()

    def yt(self):
        if self.action == "search":
            from .yt.yt import Yt
            search = Yt(self.query)
            search.search()
        if self.action == "video":
            from .yt.yt import Yt
            video = Yt(self.query)
            video.get_video()
        if self.action == "download":
            from .yt.yt import Yt
            download = Yt(self.query)
            download.dl_video()
        if self.action == "stream":
            from .yt.yt import Yt
            stream = Yt(self.query)
            stream.stream_video()

    def music(self):
        if self.action == "download":
            from .yt.yt import Yt
            download = Yt(self.query)
            download.dl_audio()
        if self.action == "stream":
            from .yt.yt import Yt
            stream = Yt(self.query)
            stream.stream_audio()

    def setting(self):
        if self.action == "help":
            from .help.help import Help
            help = Help()
            help.run_help()
        else:
            from .help.setting import Setting
            setting = Setting(self.action, self.query)
            setting.setting()