
# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48


#solution
import random

def main():
    # Generate the secret number at random!
    secret_number = random.randint(1,99)
    print("I am thinking of a number between 1 and 99...")

    # Get user's guess
    guess = int(input("Enter a guess:"))
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
             print("your guess is too high")

        print()

        guess = int(input("Enter a new guess:"))
    print("Congrats! The number was: " + str(secret_number))
if __name__ == '__main__':
    main()

