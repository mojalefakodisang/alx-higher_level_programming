#!/usr/bin/python3
def print_last_digit(number):

    if number >= 0 and number <= 9:
        n = number
    else:
        n = abs(number)
        n = str(n)
        n = n[-1]

    print('{}'.format(n), end="")

    return (n)
