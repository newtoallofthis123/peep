import os
from rich.console import Console
from rich.panel import Panel

console = Console()


class Help:
    def __init__(self):
        pass

    def help_content(self):
        from pyfiglet import Figlet
        figlet = Figlet(font="doom")
        console.print(figlet.renderText("PEEP"), style="green", justify="center")
        console.print(Panel.fit(f"{os.getlogin().capitalize()}'s PEEP: Personalized Environment and Execution Prompt",
                                title="Help", border_style="green"), justify="center")
        console.print("PEEP is the friendly assistant we have all been looking for. "
                      "PEEP lives in the command line and loves it there. And it's here to help you with"
                      " your daily tasks. PEEP is not perfect, but it's getting there. PEEP is a work in progress."
                      " PEEP is developed by [link=https://noobscience.rocks]NoobScience[/link] and is licensed under the MIT License. ")

    def run_help(self):
        self.help_content()
