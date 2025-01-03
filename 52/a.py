# duck typing - method apart from inheritance to achieve polymorphism

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Car:
    alive = False
    def speak(self):
        print("honk!")

animals = [Dog(), Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)