#!/usr/bin/env python3
"""  This will roll two dice and print out the values """
import sys
from random import randint


def rolldice():
    print()
    answer = input("Roll Dice? (y/n):")
    if (answer == "y") or (answer == ""):
        die01 = (randint(1, 6))
        die02 = (randint(1, 6))
        #print(("You rolled a:"), (die01))
        return die01, die02
    elif answer == "n":
        sys.exit(0)
    else:
        print("Invalid key pressed")
        sys.exit(1)


def main():
    die01, die02 = rolldice()
    print("die01 ", die01)
    print("die02 ", die02)
    main()


if __name__ == "__main__":
    main()
