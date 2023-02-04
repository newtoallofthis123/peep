from ..format import *
from ..brain import *
import os

class Key:
    def __init__(self):
        self.key = ""

    def ask_key(self):
        c_print("Please enter your API key for the OpenAI service\nYou can get it [link=https://beta.openai.com/account/api-keys]here[/link]", code="info")
        key = str(input("API Key: "))
        self.key = key
        home_dir = os.path.expanduser( '~' )
        os.mkdir(os.path.join(home_dir, ".peep")) if not os.path.exists(os.path.join(home_dir, ".peep")) else None
        with open(os.path.join(home_dir, ".peep", "ai.txt"), "w") as file:
            file.write(key)
        return key
    def get_key(self):
        home_dir = os.path.expanduser( '~' )
        key_file = os.path.join(home_dir, ".peep", "ai.txt")
        if os.path.exists(key_file):
            with open(key_file, "r") as file:
                key = file.read()
                self.key = key
                return key
        else:
            self.key = self.ask_key()
            return self.key