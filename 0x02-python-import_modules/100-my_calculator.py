#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = len(sys.argv) - 1
    if args < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        op = {"+": add, "-": sub, "*": mul, "/": div}
        if sys.argv[2] not in list(op.keys()):
            print("Unknown operator. Availabe operators: +, -, * and /")
            sys.exit(1)

        print("{} {} {} = {}".format(a, sys.argv[2], b, op[sys.argv[2]](a, b)))
