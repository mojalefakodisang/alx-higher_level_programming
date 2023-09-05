#!/usr/bin/python3
def print_last_digit(number):
    
    if number < 9:
        n = str(number)
        n = n[-1]
    else:
        n = number
    print(n)

    return (n)
