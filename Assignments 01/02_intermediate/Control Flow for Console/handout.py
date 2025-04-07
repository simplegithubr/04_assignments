
import random


def main():
    print("🎮 Welcome to the High-Low Game!")
    print('--------------------------------')
    
    rounds = 5
    score = 0
    for round_number in range(1, rounds + 1):
        print(f"\n--- Round {round_number} ---")
        your_number = int(input("Enter a number between 1 and 100: "))
        while your_number < 1 or your_number > 100:
            print("Invalid input! Please enter a number between 1 and 100.")
            your_number = int(input("Enter a number between 1 and 100: "))
        computer_number = random.randint(1, 100)

       
        guess = input("Do you think your number is higher or lower than the computer's? (Type 'higher' or 'lower'): ").strip().lower()
        if (guess == 'higher' and your_number > computer_number) or (guess == 'lower' and your_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"You were wrong! The computer's number was {computer_number}")
            
            
        
        print(f"Your score: {score}")
    
    print("\n--- Game Over! ---")
if __name__ == "__main__":
    main()



