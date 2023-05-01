from service.execute import *
from service.brain import *

def main():
    from rich.traceback import install
    install(show_locals=True)
    if len(sys.argv) == 1:
        from pyfiglet import Figlet
        figlet = Figlet(font="doom")
        console.print(figlet.renderText("PEEP"), style="green", justify="center")
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
    elif len(sys.argv) == 2 and sys.argv[1] not in get_ops()["args"]:
        c_print(f"Invalid argument: {sys.argv[1]}", code="danger")
        c_print("Use peep help for more info", code="info")
    else:
        args = get_args()[0]
        if args[0] in get_ops()["args"]:
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
                if do_what == "setting":
                    execute.setting()
                if do_what == "file":
                    execute.file()
                if do_what == "article":
                    execute.article()

if __name__ == '__main__':
    main()
