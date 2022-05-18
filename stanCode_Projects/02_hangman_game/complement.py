"""
File: complement.py
Name:Zoey
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    To find the complement strand of a DNA sequence.
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    dna = dna.upper()
    print('The complement of '+dna+' is '+build_complement(dna))


def build_complement(dna):
    """
    :param dna: user input
    :return new: the complement strand of a DNA sequence
    """
    new = ''
    for ch in dna:
        if ch == 'A':
            new += 'T'
        elif ch == 'T':
            new += 'A'
        elif ch == 'C':
            new += 'G'
        elif ch == 'G':
            new += 'C'
    return new


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
