#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    sum = 0
    i = 1
    while i < length:
        sum += int(sys.argv[i])
        i += 1
    print(sum)
