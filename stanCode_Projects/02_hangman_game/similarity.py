"""
File: similarity.py
Name:Zoey
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    User inputs short and long dna sequence.
    And find the most similar short dna sequence within a long dna sequence.
    """
    long_sequence = input('Please give me a DNA sequence to research: ')
    short_sequence = input('What DNA sequence would you like to match? ')
    long_sequence = long_sequence.upper()
    short_sequence = short_sequence.upper()
    print('The best match is ' + homology(long_sequence, short_sequence))


def homology(long_sequence, short_sequence):
    """
    :param long_sequence: the long dna sequence
    :param short_sequence: the short dna sequence which user would like to match
    :return best_match: the most similar short dna sequence within a long dna sequence.
    """
    len_l = len(long_sequence)
    len_s = len(short_sequence)
    n = len_l-len_s+1
    max_match_number = 0
    best_match = ""
    for i in range(n):
        sequence = long_sequence[i:i+len_s]
        match_number = 0
        for j in range(len_s):
            if sequence[j] == short_sequence[j]:
                match_number += 1
        if match_number > max_match_number:
            max_match_number = match_number
            best_match = sequence
    return best_match


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
