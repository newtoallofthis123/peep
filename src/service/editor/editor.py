import os
from ..format import *
class Editor:
    def __init__(self, file, lang):
        self.file = file
        self.lang = lang

    def exits(self):
        return os.path.exists(self.filepath())

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

    def server(self, lang, content, file_path):
        from flask import Flask, render_template, request
        app = Flask(__name__)
        @app.route("/")
        def home():
            return render_template("editor.html", lang=lang, content=content, file_path=file_path, file=self.file)

        @app.route('/write', methods=["POST"])
        def write():
            content = request.form.get("content")
            self.write(content)
            return "Wrote Content"

        app.run(port=8000)
    def open(self):
        if self.exits():
            self.server(self.lang, self.content(), self.filepath())
        else:
            print(self.filepath())
            c_print(f"File {self.file} doesn't exist", code="danger")
            return False