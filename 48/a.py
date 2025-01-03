# inheritance

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("WOOF")
class Cat(Animal):
    def speak(self):
        print("MEOW")
class Mouse(Animal):
    def speak(self):
        print("SQUEAK")

dog = Dog("Spike")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print(dog.name)
cat.eat()
mouse.sleep()

dog.speak()
cat.speak()
