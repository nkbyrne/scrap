#!/usr/bin/env python3
""" This will use the dice rolling function of dice.py to roll two dice and
    print them out in a fun way """
import sys
from random import randint
from termcolor import colored
from dice import rolldice


def gamble():
    die01, die02 = rolldice()
    print("You rolled a ", (colored(die01, "yellow")))
    answer = input("Higher or Lower (h/l):")
    if answer == "h" or (answer == ""):
        if die01 < die02:
            print("Higher")
            print("Next roll was a:", (die02), colored("Well done", "green"))
            return
        elif die01 == die02:
            print("Higher")
            print("Next roll was a:", (die02), colored("Draw!", "blue"))
            return
        else:
            print("Higher")
            print("Next roll was a:", (die02), colored("Loser", "red"))
            return
    if answer == "l":
        if die01 > die02:
            print("Lower")
            print("Next roll was a:", (die02), colored("Well done", "green"))
            return
        elif die01 == die02:
            print("Lower")
            print("Next roll was a:", (die02), colored("Draw!", "blue"))
            return
        else:
            print("Lower")
            print("Next roll was a:", (die02), colored("Loser", "red"))
            return
    else:
        print("Invalid key pressed")
        print(answer)
        sys.exit(1)


def main():
    gamble()
    main()


if __name__ == "__main__":
    main()
