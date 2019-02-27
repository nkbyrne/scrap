#!/usr/bin/env python3
import sys
from random import randint

die01 = (randint(1, 6))
die02 = (randint(1, 6))


def playagain():
    global die01
    global die02
    die01 = (randint(1, 6))
    die02 = (randint(1, 6))
    answer = input("Roll again (y/n):")
    if (answer == "y") or (answer == ""):
        main()
    elif answer == "n":
        sys.exit(0)
    else:
        print("Invalid key pressed")
        sys.exit(1)


def main():
    print(("You rolled a:"), (die01))
    playagain()


if __name__ == "__main__":
    main()
