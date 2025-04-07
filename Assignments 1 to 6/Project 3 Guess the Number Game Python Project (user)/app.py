import random

def guess_number():
    low = 1
    high = 50
    feedback = ""

    print("welcome to Number Guessing 🎮Game (User) ")
    print("Think of a number between 1 and 50, and I'll try to guess it!")

    while feedback != "c":

        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (h) , too low (l), or correct (c)? ").lower()

        if feedback == "h":
          high = guess -1
        elif feedback == "l":
          low = guess + 1

    print(f"Yay!🎉 I guessed your number {guess} correctly!")


if __name__ == "__main__":
    guess_number()