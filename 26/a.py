# concessions stand

menu = {
    "pizza" : 3.00,
    "nachos" : 2.00,
    "hot dog" : 1.00,
    "popcorn" : 1.50,
    "soda" : 1.00,
    "candy" : 1.25,
    "lemonade" : 1.00
}

cart = []
total = 0

print("----MENU-----")
for key,value in menu.items():
    print(f"{key:10} : ${value:.2f} ")
print("-------------")

while True:
    food = input("select food to buy q to quit")
    if food.lower() == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
print(cart)

for food in cart:
    total = total + menu.get(food)
    print(food , end = " ")
print(f"total is {total:.2f} $")