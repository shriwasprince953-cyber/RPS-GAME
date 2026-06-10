import random

# choices for game
choices = ["rock", "paper", "scissors"]

# user input
user = input("Enter Rock, Paper, or Scissors: ").lower()

# computer choice
computer = random.choice(choices)

print("Computer chose:", computer)

# game logic for RPS
if user == computer:
    print("It's a tie!")

elif user == "rock" and computer == "scissors":
    print("You win!")

elif user == "paper" and computer == "rock":
    print("You win!")

elif user == "scissors" and computer == "paper":
    print("You win!")

elif user in choices:
    print("Computer wins!")

else:
    print("Invalid input!")