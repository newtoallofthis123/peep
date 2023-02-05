import os
from ..format import *
class Setting:
    def __init__(self, command, query):
        self.command = command
        self.query = query

    def setting(self):
        if self.command == "reset":
            from .start import intro
            intro()
        if self.command == "edit":
            c_print("You are free to edit the settings file.", code="info")
            file_response = ask("Do you want to open the settings file?")
            if file_response:
                c_print(f'Setting File is located at: {os.path.join(os.path.dirname(__file__).strip("/service/help/"), "args.json")}', code="success")
                open_response = ask("Do you want to open the settings file?")
                if open_response:
                    from ..brain import platform
                    if platform() == "win":
                        os.system(f'start {os.path.join(os.path.dirname(__file__).strip("/service/help/"), "args.json")}')
                    else:
                        os.system(
                            f'open {os.path.join(os.path.dirname(__file__).strip("/service/help/"), "args.json")}')
                else:
                    c_print("You can edit the settings file manually.", code="info")