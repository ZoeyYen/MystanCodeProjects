"""
File: rocket.py
Name:Zoey
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 1


def main():
    """
    Build a rocket!
    """
    head(SIZE)
    belt(SIZE)
    upper(SIZE)
    lower(SIZE)
    belt(SIZE)
    head(SIZE)


def head(n):
    """
    The head part of rocket
    """
    for i in range(n):
        print(' ', end='')
        for j in range(n * 2):
            if n > j >= n - i - 1:
                print('/', end='')
            elif n + i >= j >= n:
                print('\\', end='')
            else:
                print(' ', end='')
        print('')


def belt(n):
    """
    The belt part of rocket
    """
    print('+', end='')
    for i in range(n * 2):
        print('=', end='')
    print('+')


def upper(n):
    """
    The upper part of rocket
    """
    for i in range(n):
        print('|', end='')
        for j in range(n - i - 1):
            print('.', end='')
        for k in range(2 * i + 2):
            if k % 2 == 0:
                print('/', end='')
            else:
                print('\\', end='')
        for m in range(n - i - 1):
            print('.', end='')
        print('|')


def lower(n):
    """
    The lower part of rocket
    """
    for i in range(n):
        print('|', end='')
        for j in range(i):
            print('.', end='')
        for k in range((n - i) * 2):
            if k % 2 == 0:
                print('\\', end='')
            else:
                print('/', end='')
        for m in range(i):
            print('.', end='')
        print('|')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
