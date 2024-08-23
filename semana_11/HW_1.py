# Cree una clase de `Circle` con:
#     1. Un atributo de `radius` (radio).
#     2. Un método de `get_area` que retorne su área.

# class Circle():

#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self, radius):
#         area = 3.14 * (self.radius * self.radius)
#         area_rounded = round(area, 2)
#         print(f'The area is: {area_rounded} cm2')

# circle_1 = Circle(float(input('Enter radius (cm): ')))
# circle_1.get_area(circle_1)

class Circle():

    def __init__(self, radius):
        self.radius = radius


    def get_area(self, radius):
        area = 3.14 * (self.radius * self.radius)
        area_rounded = round(area, 2)
        print(f'The area is: {area_rounded} cm2')

def ask_radius():
    while True:
        try:
            value = float(input('Enter radius (cm): '))
            return value
        except Exception as error:
            print(f'Enter valid number. {error}.')
        


circle_1 = Circle(ask_radius())
circle_1.get_area(circle_1)