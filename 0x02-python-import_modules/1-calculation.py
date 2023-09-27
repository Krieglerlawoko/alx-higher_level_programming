#!/usr/bin/python3

if __name__ == "__main__":
    """Print sum multiple difference and quotient of 5 and 10"""
    from calculator_1 import add, sub, mul, div

    b = 5
    a = 10

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
