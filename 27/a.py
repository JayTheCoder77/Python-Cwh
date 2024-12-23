#random number

import random
low = 1
high = 10
# print(help(random))
options = ("rock" , "paper" , "scissors")
cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# number = random.randint(low, high)
number = random.random()
option = random.choice(options)
random.shuffle(cards)
print(cards)