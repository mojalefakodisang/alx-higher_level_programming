#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        ch = chr(ord(ch) - 32)
        print("{:s}".format(ch), end="")

    print("\n", end="")
