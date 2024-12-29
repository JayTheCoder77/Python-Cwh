from script1 import *

def fav_drink(drink):
    print(f"your fav drink is {drink}")

def main():
    print("script 2 ")
    fav_drink("water")
    fav_food("ice cream")
    print("bye")

if __name__ == '__main__':
    main()