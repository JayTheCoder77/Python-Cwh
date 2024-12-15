# food = input("enter fav food (q to quit)")

# while not food == 'q' :
#     print(f"you like {food}")
#     food = input("enter fav food (q to quit)")
# print("bye")

num = int(input("num from 1 to 10"))

while num < 1 or num > 10 :
    print(f"{num} not valid try again")
    num = int(input("num from 1 to 10"))
print(f"{num} lies between 1 and 10")