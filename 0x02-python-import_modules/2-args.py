#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1
    if args == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(args))
        i = 1
        while i < args + 1:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
