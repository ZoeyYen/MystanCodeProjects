"""
File: hangman.py
Name:Zoey
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game.
    """
    ans = random_word()
    dashed = dash(ans)
    number = N_TURNS
    print('The word looks like: ' + dashed)
    print('You have ' + str(number) + ' guesses left.')
    while True:
        input_ch = input('Your guess: ')
        input_ch = input_ch.upper()
        if input_ch.isalpha() and len(input_ch) == 1:
            # CORRECT
            if input_ch in ans:
                guess = ''
                for i in range(len(ans)):
                    if ans[i] == input_ch:
                        guess += ans[i]
                    else:
                        guess += dashed[i]
                dashed = guess
                print('You are correct!')
            # WRONG
            else:
                number -= 1
                print("There is no "+input_ch+"'s in the word.")
            # Win!!
            if dashed == ans:
                print('You win!!')
                break
            # Game over
            elif number == 0:
                print('You are completely hung :(')
                break
            print('The word looks like: ' + dashed)
            print('You have ' + str(number) + ' guesses left.')
        else:
            print('illegal format.')
    print('The word was: ' + ans)


def dash(ans):
    """
    return the same length of dash as ans
    """
    dashed = ""
    for i in range(len(ans)):
        dashed += "_"
    return dashed


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
