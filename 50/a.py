# super function
class Shape:
    def __init__(self, color,filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")


class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius = radius

    def describe(self):
        print(f"Area is {3.14 * self.radius * self.radius} cm2")
        super().describe()


class Square(Shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width = width

    def describe(self):
        print(f"Area is {self.width * self.width} cm2")
        super().describe()


class Triangle(Shape):
    def __init__(self,color,filled,width,height):
        super().__init__(color,filled)
        self.width = width
        self.height = height




circle = Circle("RED",True,5)
square = Square("Blue",False,5.9)
triangle = Triangle("GREEN",True,10,9.2)

circle.describe()
square.describe()
triangle.describe()

# print(circle.color)
# print(circle.filled)
# print(f"{circle.radius} cm")

# print(square.color)
# print(square.filled)
# print(square.width)

# print(triangle.color)
# print(triangle.filled)
# print(triangle.width)
# print(triangle.height)