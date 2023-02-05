import os


def dir_make(file):
    import os
    home_dir = os.path.expanduser('~')
    os.mkdir(os.path.join(home_dir, ".peep")) if not os.path.exists(os.path.join(home_dir, ".peep")) else None
    return os.path.join(home_dir, ".peep", file)


def check_intro():
    if os.path.exists(dir_make("intro.txt")) and open(dir_make("intro.txt"), "r").read() == "True":
        return True
    else:
        with open(dir_make("intro.txt"), "w") as file:
            file.write("True")
        return False


def check_reqs():
    import sys
    import subprocess
    import pkg_resources
    print("Checking for requirements...")
    required = {'flask', 'rich', 'pyqrcode', 'pyzbar', 'segno', 'openai', 'pypng'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed
    if missing:
        install_response = input(f"Peep requires {missing} to run. Do you want to install them? (y/n): ")
        if install_response == "y":
            python = sys.executable
            subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
        elif install_response == "n":
            print("Peep will not work without the required packages.")
            exit()
        else:
            print("Invalid Response")
            exit()


def set_alias():
    import os
    import platform
    if platform.system() == "Windows":
        os.system("doskey peep=python " + os.path.join(os.getcwd(), "src", "main.py") + " $*")
        print("Alias set! on cmd. To set it on powershell, run the command: "
              "Set-Alias -Name peep -Value python " + os.path.join(os.getcwd(), "src", "main.py") + " $*")
    elif platform.system() in ["Linux", "Darwin"]:
        os.system("alias peep=python " + os.path.join(os.getcwd(), "src", "main.py") + " $*")
        print("Alias set!")
    else:
        print("Your platform is not supported for aliasing.")
def intro():
    open(dir_make("intro.txt"), "w").write("False")
    if not check_intro():
        print("Welcome to Peep!")
        print("Peep is a CLI based tool to make command line easier!")
        print("Peep is developed by: https://noobscience.rocks and is licensed under the MIT License")
        check_reqs()
        print("Peep is ready to use!")
        from rich.prompt import Confirm
        alias_response = Confirm.ask("Do you want to set an alias for Peep?")
        if alias_response:
            set_alias()
        else:
            print("You can set an alias later by running the command: peep run alias")
    else:
        print("Welcome back to Peep!")
        print("Seems you have already used Peep before. Skipping requirements check...")
        print("Peep is ready to use!")
        print("If your alias is not working, run the command: peep run alias")
        print("If you want to reset your intro, run the command: peep run reset\n")