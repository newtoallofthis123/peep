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
    if len(sys.argv[2:]) == 0:
        return sys.argv[1]
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

import socket
from contextlib import closing

def port_check(port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex(('127.0.0.1', port)) == 0:
            return True
        else:
            return False

def port_assign():
    choices = [i for i in range(5000, 6000)]
    for i in choices:
        if port_check(i):
            c_print(f"Port {i} is in use, trying next port...", code="warning")
            continue
        else:
            c_print(f"Port {i} is available, using it...", code="success")
            return i