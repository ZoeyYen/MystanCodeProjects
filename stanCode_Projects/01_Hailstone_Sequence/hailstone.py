"""
File: hailstone.py
Name:Zoey
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program shows Hailstone sequence.
    """
    print('This program computes Hailstone sequences.')
    n = int(input('Enter a number: '))
    # i : record the number of steps
    i = 0
    while n != 1:
        if n % 2 == 0:
            a = n//2
            print(str(n) + ' is even, so I take half: ' + str(a))
        else:
            a = 3*n+1
            print(str(n) + ' is odd, so I make 3n+1: ' + str(a))
        n = a
        i += 1
    print('It took '+str(i)+' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
