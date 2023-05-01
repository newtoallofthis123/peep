import os, json
from rich.console import Console
from rich.panel import Panel

console = Console()

does = {
    "search": "Searches the web for the query",
    "editor": "Opens the web based text editor",
    "md": "Converts the query to markdown",
    "ai": "Opens the AI",
    "qr": "Converts the query to QR Code",
    "img_qr": "Converts the image to QR Code",
    "yt": "Searches YouTube for the query and streams the video",
    "music": "Search music and play in the custom player",
    "setting": "Opens the Settings",
    "article": "Downloads the article from the web",
}

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
        console.print("Available commands:", style="bold red underline")
        from rich import print_json
        print_json(data=json.loads(str(does).replace("'", '"')))
        console.print("It is easier to represent PEEP commands in a HTML file.", style="bold")
        from ..format import ask
        from ..brain import platform
        internet_response = ask("Are you connected to the internet?:")
        if internet_response:
            if platform() == "win":
                os.system("start https://peep.noobscience.rocks")
            else:
                os.system("open https://peep.noobscience.rocks")
    def run_help(self):
        self.help_content()
