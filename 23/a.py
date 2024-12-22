# 2d lists

fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "lettuce", "onion"]
meats = ["lamb", "chicken", "pork"]

groceries = [fruits, vegetables, meats]

for item in groceries:
    for i in item:
        print(i , end="->")
    print()