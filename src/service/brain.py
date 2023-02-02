import json
import os
import sys
import pyperclip
from .format import *
def get_ops():
    with open(os.path.join(os.path.dirname(__file__), "args.json"), "r") as file:
        options = json.loads(file.read())
        return options
def get_args():
    if len(sys.argv[1:]) == 0:
        return None
    else:
        args = sys.argv[1:]
        query = ' '.join(sys.argv[3:])
        return ((args[0], args[1]), query)

def copy(text):
    c_print(f"Copying {text} to clipboard...")
    pyperclip.copy(text)

def platform():
    import platform

    if platform.system() == "Windows":
        return "win"
    elif platform.system() in ["Linux", "Darwin"]:
        return "unix"
    else:
        return None

def cls():
    if platform() == "win":
        os.system("cls")
    elif platform() == "unix":
        os.system("clear")
    else:
        pass