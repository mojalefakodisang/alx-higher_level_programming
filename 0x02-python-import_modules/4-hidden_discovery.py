#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4, sys

    for char in dir(hidden_4):
        if char[:2] != "__":
            print("{:s}".format(char))
