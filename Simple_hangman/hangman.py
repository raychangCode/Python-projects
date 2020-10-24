"""
File: hangman.py
Name: Ray Chang, 2020.08
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    a. when to break : 1. win 2. N_TURNS=0
    b.
    while true
    1. g = guess(), make a guess

    2. if ans.find(g) != -1
            if guess was correct
    3. elif exception
            illegal format
    4. if ans.find(g) == 1
            guess was wrong
            n -= 1

    """
    n = N_TURNS
    ans = random_word()

    tmp = ''
    for i in range(len(ans)):
        tmp += '-'

    while True:
        print("The word looks like: " + tmp)
        print("You have " + str(n) + " guesses left.")
        g = input("your guess:")
        g1 = g.upper()

        if ans.find(g1) != -1:
            print("You are correct!")
            tmp1 = '' #create an empty string to store the correct guess
            for j in range(len(tmp)):
                if g1 == ans[j]:
                    tmp1 += g1
                else:
                    #tmp[j] is the current answer
                    tmp1 += tmp[j]
            tmp = tmp1
            if tmp == ans:
                print("You Win !!")
                print("The word was:" + ans)
                break
        elif not g1.isalpha() or len(g1) > 1:
            print("illegal format.")
        else:
            n -= 1
            print("There is no " + g1 + "'s in the word.")
            if n <= 0:
                print("You are completely hung :(")
                print("The word was:" + ans)
                break


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
