# Dice Roller

import random
dice_art = {
    1: (
        "  -----",
        " |     |",
        " |  o  |",
        " |     |",
        "  -----",
    ),
    2: (
        "  -----",
        " | o   |",
        " |     |",
        " |   o |",
        "  -----",
    ),
    3: (
        "  -----",
        " | o   |",
        " |  o  |",
        " |   o |",
        "  -----",
    ),
    4: (
        "  -----",
        " | o o |",
        " |     |",
        " | o o |",
        "  -----",
    ),
    5: (
        "  -----",
        " | o o |",
        " |  o  |",
        " | o o |",
        "  -----",
    ),
    6: (
        "  -----",
        " | o o |",
        " | o o |",
        " | o o |",
        "  -----",
    ),
}

dice = []
total = 0
num = int(input("how many dice?"))
for die in range(num):
    dice.append(random.randint(1,6))

# for die in range(num):
#     for line in dice_art.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end=" ")
    print()


for die in dice:
    total += die
print(f"Total : {total}")