# @property

class Rectangle:
    def __init__(self, width, height):
        self._width = width     # protected member 
        self._height = height   # protected member

    @property
    def width(self):
        return f"{self._width:.1f} cm"
    @property
    def height(self):
        return f"{self._height:.1f} cm"
    @width.setter
    def width(self,new_width):
        if new_width > 0 :
            self._width = new_width
        else:
            print("invalid width")
    @height.setter
    def height(self,new_height):
        if new_height > 0 :
            self._height = new_height
        else:
            print("invalid height")
    @width.deleter
    def width(self):
        del self._width
        print("Deleting...")



rectangle = Rectangle(10.981, 20.345)

rectangle.width = 90.345

print(rectangle.width)
del rectangle.width
# print(rectangle.width)
print(rectangle.height)
