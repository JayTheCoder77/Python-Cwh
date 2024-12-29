# if name = __main__

# from script2 import *
# print(__name__)

def fav_food(food):
    print(f"fav food is {food}")

def main():
    print("script 1")
    fav_food("pizza")

if __name__ == '__main__':
    main()