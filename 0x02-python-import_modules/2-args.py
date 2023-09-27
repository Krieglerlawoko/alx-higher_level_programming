#!/usr/bin/python3

if __name__ == "__main__":
    """Print out  no. of and list of arguments."""
    import sys

    cnt = len(sys.argv) - 1
    if cnt == 1:
        print("1 argument:")
    elif cnt == 0:
        print("0 argument:")
    else:
        print("{} arguments:".format(count))
    for k in range(cnt):
        print("{}: {}".format(k + 1, sys.argv[k + 1]))
