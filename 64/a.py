#multithreading

import threading
import time

def walk_dog(first):
    time.sleep(8)
    print(f"You finish walking {first}")

def take_trash():
    time.sleep(2)
    print("You take out trash")

def get_mail():
    time.sleep(3)
    print("you get mail")


chore1 = threading.Thread(target = walk_dog ,args = ("spike",)) # comma neccessary
chore1.start()

chore2 = threading.Thread(target = take_trash)
chore2.start()

chore3 = threading.Thread(target = get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()
print("all chores complete")
