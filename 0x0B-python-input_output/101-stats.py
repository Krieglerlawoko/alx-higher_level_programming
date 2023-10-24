#!/usr/bin/python3
"""Reads standard input"""


def print_stats(size, status_codes):
    """Print metrics accumulated"""
    print("File size: {}".format(size))
    for j in sorted(status_codes):
        print("{}: {}".format(j, status_codes[j]))


if __name__ == "__main__":
    import sys

    status_codes = {}
    size = 0
    c = 0
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

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
