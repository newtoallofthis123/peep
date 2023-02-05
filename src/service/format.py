from rich.console import Console
from rich.theme import Theme
from rich.prompt import Confirm, Prompt

theme = Theme({
    "info": "bold cyan",
    "warning": "magenta",
    "danger": "bold red",
    "success": "bold green",
    "normal": ""
})
console = Console(theme=theme)
def c_print(text, code):
    console.print(text, style=code)

def ask(text):
    ask_response = Confirm.ask(text, default=True)
    return ask_response

def prompt(text):
    prompt_response = Prompt.ask(text)
    return prompt_response