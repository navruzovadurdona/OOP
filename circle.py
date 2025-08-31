"""Класс "Круг"
Создай класс Circle, который вычисляет площадь и длину окружности по радиусу.
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius

circle1 = Circle(5)
print(f"Площадь круга с радиусом {circle1.radius} равна {circle1.area()}")
print(f"Длина окружности круга с радиусом {circle1.radius} равна {circle1.circumference()}")
