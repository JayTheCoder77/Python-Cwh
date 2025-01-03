#multiple and multilevel inheritance

class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")
    
class Rabbit(Prey):
    pass

class Eagle(Predator):
    pass

class Fish(Prey,Predator):
    pass


r = Rabbit("Bugs")
e = Eagle("TONY")
f = Fish("NEMO")

r.flee()
f.flee()
f.hunt()
e.hunt()
r.eat()
e.eat()
f.eat()

