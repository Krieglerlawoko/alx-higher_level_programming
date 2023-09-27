#!/usr/bin/python3

if __name__ == "__main__":
    """Prints names"""
    import hidden_4

    nam = dir(hidden_4)
    for n in nam:
        if n[:2] != "__":
            print(nam)
