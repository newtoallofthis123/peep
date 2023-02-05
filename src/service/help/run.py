import os
class Run:
    def __init__(self, command):
        self.command = command
        self.help = os.path.join(os.path.dirname(__file__), "README.md")

    def run(self):
        if self.command == "help":
            with open(self.help, "r") as help_file:
                help_file = help_file.read()
                from rich.console import Console
                from rich.markdown import Markdown

                console = Console()
                md = Markdown(help_file)
                console.print(md)