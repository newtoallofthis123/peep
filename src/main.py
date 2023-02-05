import sys
from service.execute import *
from service.brain import *
def main():
    if len(sys.argv) == 1:
        c_print("No arguments provided, exiting...\nUse peep help for more info", code="danger")
        response = prompt("Type 'help' to get help, press any key to exit")
        if response.lower() == "help":
            from service.help.help import Help
            help = Help()
            help.run_help()
        else:
            sys.exit(1)
    elif get_args() == "help":
        from service.help.help import Help
        help = Help()
        help.run_help()
    else:
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
            if do_what == "img_qr":
                execute.img_qr()
            if do_what == "yt":
                execute.yt()
            if do_what == "music":
                execute.music()
            if do_what == "set":
                execute.set()

if __name__ == '__main__':
    main()