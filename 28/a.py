#number guessing game

import random

lowest = 1
highest = 100

answer = random.randint(lowest, highest)
# print(answer)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Guess a number between {lowest} and {highest}")

while is_running:
    guess = input("Guess")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest or guess > highest:
            print("enter again out of bounds guess")
        elif guess < answer:
            print("too low")
        elif guess > answer:
            print("too high")
        else:
            print(f"you guessed {answer} in {guesses} guesses")
            is_running = False
    else:
        print("invalid guess")