#python quiz game

questions = ("what is the 5th element of the periodic table?",
             "what is the capital of Nigeria?",
             "what is the capital of Ghana?",
             "what is the capital of Kenya?",
             "what is the capital of South Africa?")

options = (("Hydrogen", "Helium", "Lithium", "Beryllium"),("Lagos", "Abuja", "Kano", "Ibadan"),("Accra", "Kumasi", "Tamale", "Takoradi"),("Nairobi", "Mombasa", "Kisumu", "Nakuru"),("Cape Town", "Johannesburg", "Pretoria", "Durban"))

answers = (("Beryllium",),("Abuja",),("Accra",),("Nairobi",),("Pretoria"))

guesses = []

score = 0
ques_num = 0

for question in questions:
    print("-----")
    print(question)
    for option in options[ques_num]:
        print(option)
    guess = input("guess option")
    guesses.append(guess)
    if guess == answers[ques_num]:
        score += 1
        print("correct")
    else:
        print("wrong")
    ques_num += 1

print("your score is", score)
