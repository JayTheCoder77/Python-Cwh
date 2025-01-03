class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"{self.model} -> 🏎   Vroom Vroom")
    def stop(self):
        print(f"{self.model} -> 🏎   STOP")
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
