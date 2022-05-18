"""
File: caesar.py
Name:Zoey
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program decrypts the caesar cipher.
    """
    n = int(input('Secret number: '))
    cipher = input("What's the ciphered string? ")
    cipher = cipher.upper()
    print('The deciphered string is: '+decipher(n, cipher))


def decipher(n, cipher):
    """
    :param n : the secret number
    :param cipher : the ciphered string
    :return ans : the decipher string
    """
    new_alphabet = ALPHABET[26 - n:] + ALPHABET[:26 - n]
    ans = ''
    for ch in cipher:
        if ch not in ALPHABET:
            ans += ch
        else:
            index = new_alphabet.find(ch)
            ans += ALPHABET[index]
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
