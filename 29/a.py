# rock paper scissors

import random

options = ("rock", "paper", "scissors")

run = True
while run:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter rock, paper or scissors: ")
    print(f"Player:{player}")
    print(f"Computer:{computer}")

    if player == computer:
        print("Tie")
    elif player == "rock" and computer == "scissors":
        print("Player wins")
    elif player == "paper" and computer == "rock":
        print("Player wins")
    elif player == "scissors" and computer == "paper":
        print("Player wins")
    else:
        print("Computer wins")
    if input("play again (y)? q to quit") == 'q':
        run = False

