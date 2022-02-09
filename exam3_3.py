class Rectangle:
    def __init__(self, length, height):
        self.__length = length
        self.__height = height

    def get_area(self):
        return self.__length * self.__height

    def get_perimeter(self):
        return (self.__height + self.__length) * 2

    @property
    def show_info(self):
        return f'Area: {self.get_area()} \nPerimeter: {self.get_perimeter()}'

rec1 = Rectangle(4, 3)
print(rec1.show_info)
