import os
from ..format import *


class File:

    def __init__(self, file):
        self.path = os.path.join(os.getcwd(), file)
        self.file = file

    def create(self):
        with open(self.path, "w") as file:
            file.write(
                "# This is a file created by Peep. You can edit this file as you wish. Just run peep run " + self.file + " to run this file.")

    def check_file(self):
        if not os.path.exists(self.path):
            c_print("File " + self.file + " does not exist. Creating...", code="warning")
            self.create()
        else:
            pass

    def file_exists(self):
        if os.path.exists(self.path):
            return True
        else:
            return False

    def get_lang(self):
        from ..brain import get_ops
        file_ext = "." + str(self.file).split('.')[1]
        file_lang = get_ops()["file_stuff"][file_ext]
        return file_lang

    def get_run(self):
        from ..brain import get_ops
        file_run = get_ops()["file_run"][self.get_lang()]
        return file_run

    def run(self):
        from rich.console import Console
        from rich.panel import Panel
        self.check_file()
        c_print("Trying to run " + self.file, code="info")
        c_print("Run peep editor " + self.file + " " + self.get_run(), code="warning")
        c_print("Detected to run " + self.file + " with " + self.get_run(), code="success")
        if self.get_run() == "default":
            os.startfile(self.path)
        else:
            import subprocess
            c_print("Running Command " + self.get_run() + " " + self.path, code="info")
            response = subprocess.run([self.get_run(), self.path], stdout=subprocess.PIPE).stdout.decode('utf-8')
            Console().print(Panel.fit(response, title="Output"), style="yellow on black")
            response_errors = subprocess.run([self.get_run(), self.path], stderr=subprocess.PIPE, stdout=subprocess.PIPE).stderr.decode('utf-8')
            Console().print(Panel.fit(response_errors, title="Errors"), style="red on black")
        c_print("Done Running " + self.file, code="success")

    def delete(self):
        if self.file_exists():
            os.remove(self.path)
            c_print("Deleted " + self.file, code="success")
        else:
            c_print("File " + self.file + " does not exist", code="danger")

    def edit(self):
        from ..editor.editor import Editor
        self.check_file()
        c_print(f"Trying to Open {self.file} in SnakeRun Editor", code="info")
        editor_instance = Editor(self.file, self.get_lang())
        editor_instance.open()