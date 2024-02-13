#!/usr/bin/python3

if __name__ == "__main__":
    """calculates."""
    import sys
    from calculator_1 import sub, add, mul, div

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    j = int(sys.argv[1])
    k = int(sys.argv[3])
    print("{} {} {} = {}".format(j, sys.argv[2], k, ops[sys.argv[2]](j, k)))
