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