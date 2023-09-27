#!/usr/bin/python3

if __name__ == "__main__":
    """addition of all arguments."""
    import sys

    sums = 0
    for k in range(len(sys.argv) - 1):
        sums += int(sys.argv[k + 1])
    print("{}".format(sums))
