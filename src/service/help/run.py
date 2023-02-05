import os
class Run:
    def __init__(self, command):
        self.command = command
        self.help = os.path.join(os.path.dirname(__file__), "README.md")

    def run(self):
        if self.command == "reset":
            from .start import intro
            intro()