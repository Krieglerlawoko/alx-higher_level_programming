#!/usr/bin/python3

def print_last_digit(number):
    """retruns and prints last digit of a number"""
    num = number
    print(abs(num) % 10, end="")
    return (abs(num) % 10)
