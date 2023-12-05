#!/usr/bin/python3
"""Reads standard input and computes metrics"""


def print_stats(size, status_codes):
    """accumulated metrics printed"""
    print("File size: {}".format(size))
    for k in sorted(status_codes):
        print("{}: {}".format(k, status_codes[k]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    c = 0

    try:
        for l in sys.stdin:
            if c == 10:
                print_stats(size, status_codes)
                c = 1
            else:
                c += 1

            l = l.split()

            try:
                size += int(l[-1])
            except (IndexError, ValueError):
                pass

            try:
                if l[-2] in valid_codes:
                    if status_codes.get(l[-2], -1) == -1:
                        status_codes[l[-2]] = 1
                    else:
                        status_codes[l[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
