#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = len(sys.argv) - 1
    if args != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]

        if op == "+":
            print("{0} + {1} = {2}".format(a, b, add(a, b)))
        elif op == "-":
            print("{0} - {1} = {2}".format(a, b, sub(a, b)))
        elif op == "*":
            print("{0} * {1} = {2}".format(a, b, mul(a, b)))
        elif op == "/":
            print("{0} / {1} = {2}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Availabe operators: +, -, * and /")
            sys.exit(1)
