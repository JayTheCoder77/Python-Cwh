# hangman game
import random
words = ("apple" , "orange" , "banana" , "grape" , "peach")

hangman_art = {
    0: (
        "   _____ ",
        "  |     |",
        "        |",
        "        |",
        "        |",
        "        |",
        "________|_",
    ),
    1: (
        "   _____ ",
        "  |     |",
        "  O     |",
        "        |",
        "        |",
        "        |",
        "________|_",
    ),
    2: (
        "   _____ ",
        "  |     |",
        "  O     |",
        "  |     |",
        "        |",
        "        |",
        "________|_",
    ),
    3: (
        "   _____ ",
        "  |     |",
        "  O     |",
        " /|     |",
        "        |",
        "        |",
        "________|_",
    ),
    4: (
        "   _____ ",
        "  |     |",
        "  O     |",
        " /|\\    |",
        "        |",
        "        |",
        "________|_",
    ),
    5: (
        "   _____ ",
        "  |     |",
        "  O     |",
        " /|\\    |",
        " /      |",
        "        |",
        "________|_",
    ),
    6: (
        "   _____ ",
        "  |     |",
        "  O     |",
        " /|\\    |",
        " / \\    |",
        "        |",
        "________|_",
    ),
}

def display_man(wrong_guesses):
    print("*************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))
    
def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("guess a letter").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("enter a single letter")
            continue

        if guess in guessed_letters:
            print("already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("win")
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("lose")
            is_running = False

if __name__ == '__main__':
    main()
