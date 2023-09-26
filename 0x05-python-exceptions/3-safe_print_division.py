#!/usr/bin/python3
def safe_print_division(a, b):
    """ Divides two integers and print the result

        Args:
            a: numerator
            b: denominator

        Return:
            returns the value of division else None
    """
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
