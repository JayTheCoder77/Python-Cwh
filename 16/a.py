# name = input("enter name")
age = int(input("enter age"))

# while name == "" :
#     print("didnt enter name")
#     name = input("enter name")
# print(f"Hello {name}")

while age < 0 :
    print("negative age invalid")
    age = int(input("enter age"))
print(f"you are {age} yrs old")