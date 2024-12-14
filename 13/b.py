user_input = input("input string")

# spaces = user_input.find(" ")  is alpha also checks for spaces 
digits = user_input.isalpha()
size = len(user_input)

if size <= 12 and digits:
    print("valid user i/p congrats 🎉🥳")
else :
    print("invalid user input")