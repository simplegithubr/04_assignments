
import random


user_number = random.randint(1, 100)
guess = 0
attempts = 0
def main():
    global user_number, guess, attempts
    while guess != user_number:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess < user_number:
            print("Too low!")
        elif guess > user_number:
            print("Too high!")
    print(f"Congratulations! You guessed the number {user_number} in {attempts} attempts.")
    print("Thanks for playing!")
if __name__ == "__main__":
    main()