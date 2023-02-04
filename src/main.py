import sys
from service.execute import *
from service.brain import *
def main():
    args = get_args()[0]
    query = get_args()[1]
    execute = Execute(args[1], query)
    do_what = args[0]
    if do_what in get_ops()["args"]:
        if do_what == "search":
            execute.search()
        if do_what == "editor":
            execute.editor()
        if do_what == "md":
            execute.md()
        if do_what == "ai":
            execute.ai()
        if do_what == "qr":
            execute.qr()

if __name__ == '__main__':
    main()