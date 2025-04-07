
import random

def guess_the_number():
    secret_number = random.randint(1, 50)
    attempts = 0

    print("🎯 Welcome to 'Guess the Number' Game!")
    print("I have selected a number between 1 and 50. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again. 🔼")
            elif guess > secret_number:
                print("Too high! Try again. 🔽")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts. 🎯")
                break
        except ValueError:
            print("❌ Invalid input! Please enter a number between 1 and 100.")

# Game start
guess_the_number()
