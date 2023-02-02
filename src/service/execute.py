from .brain import *
from urllib.parse import quote
from .format import *
from editor.editor import *
import webbrowser
import os

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
        editor = Editor()