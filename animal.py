"""Наследование: животные
Создай базовый класс Animal с методом make_sound(). Создай два подкласса Dog и Cat, которые переопределяют этот метод."""

class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Гав!")

class Cat(Animal):
    def make_sound(self):
        print("Мяу!")

dog = Dog()
cat = Cat()

dog.make_sound()  
cat.make_sound()  
