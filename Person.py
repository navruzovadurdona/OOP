"""Класс "Человек"
Создай класс Person, у которого есть имя, возраст, и метод say_hello(), который выводит приветствие."""

class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def say_hello(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет.")


person1 = Person("Durdona", 17)
person1.say_hello()
