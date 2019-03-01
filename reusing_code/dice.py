#!/usr/bin/env python3
import sys
from random import randint

die01 = ()
die02 = ()


def rolldice():
    print()
    answer = input("Roll Dice? (y/n):")
    if (answer == "y") or (answer == ""):
        die01 = (randint(1, 6))
        die02 = (randint(1, 6))
        print(("You rolled a:"), (die01))
        return die01, die02
    elif answer == "n":
        sys.exit(0)
    else:
        print("Invalid key pressed")
        sys.exit(1)


def main():
    while True:
        rolldice()


if __name__ == "__main__":
    main()
