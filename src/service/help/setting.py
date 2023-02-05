import os
class Setting:
    def __init__(self, command):
        self.command = command

    def setting(self):
        if self.command == "reset":
            from .start import intro
            intro()