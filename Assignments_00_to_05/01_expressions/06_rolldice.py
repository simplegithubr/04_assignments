
# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.

# Solution

import random
NUM_SIDES: int = 6

def main():
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2

    print("Diece have" , NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

if __name__ == "__main__":
    main()
    