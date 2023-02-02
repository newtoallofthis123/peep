import os
from .web import *
from ..format import *
class Editor:
    def __init__(self, file, lang):
        self.file = file
        self.lang = lang

    def exits(self):
        return os.path.exists(self.file)

    def filepath(self):
        return os.path.join(os.path.dirname(__file__), self.file)
    def content(self):
        if self.exits():
            with open(os.path.join(os.path.dirname(__file__), self.file), "r") as file:
                content = file.read()
                return content
        else:
            return None
    def write(self, content):
        with open(os.path.join(os.path.dirname(__file__), self.file), "w") as file:
            file.write(content)
            return True

    def open(self, content):
        if self.exits():
            if content is None:
                content = self.content()
            # server(self.lang, content)
        else:
            c_print(f"File {self.file} doesn't exist", code="danger")
            return False