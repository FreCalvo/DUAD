# 2. Cree una clase abstracta de `Shape` que:
#     1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
#     2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
#     3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod
import os

class Shape():

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    
    def calculate_perimeter(self, radius):
        perimeter = 2 * 3.14 * radius
        rounded_perimeter = round(perimeter, 3)
        print(f'Circle perimeter is: {rounded_perimeter}')

    def calculate_area(self, radius):
        area = 3.14 * (radius * radius)
        rounded_area = round(area, 3)
        print(f'Circle area is: {rounded_area}')

    def calculate_perimeter_and_area(self, radius):
        self.calculate_perimeter(radius)
        self.calculate_area(radius)


class Square(Shape):
    def calculate_perimeter(self, side):
        perimeter = side * 4
        rounded_perimeter = round(perimeter, 3)
        print(f'Square perimeter is: {rounded_perimeter}')

    def calculate_area(self, side):
        area = side * side
        rounded_area = round(area, 3)
        print(f'Square area is: {rounded_area}')

    def calculate_perimeter_and_area(self, side):
        self.calculate_perimeter(side)
        self.calculate_area(side)


class Rectangle(Shape):
    def calculate_perimeter(self, length, width):
        perimeter = (2 * length) + (2 * width)
        rounded_perimeter = round(perimeter, 3)
        print(f'Rectangle perimeter is: {rounded_perimeter}')

    def calculate_area(self, length, width):
        area = length * width
        rounded_area = round(area, 3)
        print(f'Rectangle area is: {rounded_area}')

    def calculate_perimeter_and_area(self, length, width):
        self.calculate_perimeter(length, width)
        self.calculate_area(length, width)

def main():
    os.system('clear')
    print()
    circle_1 = Circle()
    circle_1.calculate_perimeter_and_area(17)
    print()

    square_1 = Square()
    square_1.calculate_perimeter_and_area(75)
    print()

    rectangle_1 = Rectangle()
    rectangle_1.calculate_perimeter_and_area(51,97)
    print()

main()


