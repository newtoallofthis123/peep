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
            print(i)
            continue
        else:
            print("Done:" +  str(i))
            return i

port_assign()