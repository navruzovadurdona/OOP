from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2



rectangle = Rectangle(5, 10)
triangle = Triangle(4, 8)
circle = Circle(3)

print(f"Площадь прямоугольника: {rectangle.area()}")
print(f"Площадь треугольника: {triangle.area()}")
print(f"Площадь круга: {circle.area()}")
