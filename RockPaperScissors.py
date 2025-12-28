import random

choices = ["rock", "paper", "scissors"]
play = True

while play:

    user_input = input("Enter either rock, paper or scissors: ")

    computer_input = random.choice(choices)

    if computer_input == user_input.lower():
        print("Draw. The computer picked ", computer_input)
    elif user_input.lower() == "rock" and computer_input == "scissors":
        print("You won! The computer picked ", computer_input)
    elif user_input.lower() == "paper" and computer_input == "rock":
        print("You won! The computer picked ", computer_input)
    elif user_input.lower() == "scissors" and computer_input == "paper":
        print("You won! The computer picked ", computer_input)
    else:
        print("You lost. The computer picked ", computer_input)

    q = input("Would you like to play again?(yes/no): ")
    if q.lower() == "no":
        play = False
    else:
        play = True
print("Bye!")

        