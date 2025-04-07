
import random
def main():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    winning_score = 5

    while True:
        user_choice = input(f"Enter rock, paper, or scissors , (or 'quit'to stop ) ").lower()
        if user_choice == "quit":
           print(f"Final Score -> You: {user_score}, computer: {computer_score}")
           print("Thanks for Playing!")
           break
        if user_choice not in choices:
           print("Invaild choise try again!")
           continue
        computer_choice = random.choice(choices)
        print(f"Computer_choice: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")

        elif (user_choice == "rock" and computer_choice == "scissors")or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
              print("You win")
              user_score += 1
        else:
             print("Computer Wins!")
             computer_score += 1

        print(f"Score -> You: {user_score} computer: {computer_score}\n")


        if user_score == winning_score:
          print("🎉 YOU ARE THE CHAMPION! 🏆")
          break
        elif computer_score == winning_score:
          print("😢 Computer won the game! Try again next time!")
          break

if __name__ == "__main__":
    main()