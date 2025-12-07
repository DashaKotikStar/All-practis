# Полиморфизм

'''#Пример 1
num_1 = 1
num_2 = 1
print(num_1 + num_2) #2
str_1 = "Py"
str_2 = "Hello_world"
print(str_1 + " " + str_2)

#Пример 2
print(len("Programming"))
print(len([1, 2, 3, 4, 5]))
print(len({1: "a", 2: "b"}))'''

'''#Пример 3
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Меня зовут: {self.name},"
              f"Мне {self.age}")
    def make_sound(self):
        print("Мяу")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Меня зовут: {self.name},"
              f"Мне {self.age}")
    def make_sound(self):
        print("Гав")
#MAIN
cat = Cat(name:"Барисик", age:10)
dog = Dog(name:"Шарик", age:5)
for animal in (cat, dog):
    animal.make_sound()
    animal.info()
    animal.make_sound()'''

#Пример 4
from math import sqrt, pi
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass
    def fact(self):
        return "I am two-dimensional shap"
    def __str__(self):
        return self.name
class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length
    def area(self):
        return self.length**2
    def fact(self):
        return "Square hane each agle aqual to 90 degrees"
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return pi*self.radius**2

#MAIN
a = Square(4)
b = Circle(7)
for fig in (a, b):
    print(fig)
    print(fig.fact())
    print(fig.area())