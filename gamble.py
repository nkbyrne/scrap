#!/usr/bin/env python3
import sys
from dice import die01, die02, playagain


def main():
    while True:
        print(("You rolled a:"), (die01))
        answer = input("Higher or Lower (h/l):")
        if answer == "h":
            if die01 < die02:
                print("Next roll was a:", (die02), ("Well done"))
                playagain()
            elif die01 == die02:
                print("Draw!")
                playagain()
            else:
                print("Next roll was a:", (die02), ("Loser"))
                playagain()
        if answer == "l":
            if die01 > die02:
                print("Next roll was a:", (die02), ("Well done"))
                playagain()
            else:
                print("Next roll was a:", (die02), ("Loser"))
                playagain()
        else:
            print("Invalid key pressed")
            sys.exit(1)


if __name__ == "__main__":
    main()
