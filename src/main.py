import sys
from service.execute import *
from service.brain import *
def main():
    args = get_args()[0]
    query = get_args()[1]

    act(args, query)

if __name__ == '__main__':
    main()