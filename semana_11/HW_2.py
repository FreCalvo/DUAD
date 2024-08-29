# Cree una clase de `Bus` con:
#     1. Un atributo de `max_passengers`.
#     2. Un método para agregar pasajeros uno por uno (que acepte una instancia de `Person` como parámetro). **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
#     3. Un método para bajar pasajeros uno por uno (en cualquier orden).

import os

# Clase Persona para guardar usuario del bus.
class Person:
    def __init__(self, qty):
        self.qty = qty

# Clase Bus.
class Bus:
    # Constructor con información de máxima capacidad y cantidad de pasajeros.
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.qty_passengers = 0


    # Método para agregar pasajeros.
    def add_passenger(self, person):
        if self.qty_passengers < self.max_passengers:
            self.qty_passengers += 1
            print('_______________________________________')
            print(f"{person.qty} passenger was added. ")
            print()
        else:
            print('_______________________________________')
            print("Bus is full.")
            print()


    # Método para restar pasajeros.
    def remove_passenger(self):
        if self.qty_passengers:
            self.qty_passengers -= 1
            print('_______________________________________')
            print("one passenger left the bus.")
            print()
        else:
            print('_______________________________________')
            print("Bus is empty.")
            print()

    # Método para mostrar espacios aún disponibles.
    def seats_available(self):
        seats_available = self.max_passengers - self.qty_passengers
        print(f'{seats_available} out of {self.max_passengers} seats still available')
        print('_______________________________________')
        print()

# Función Main que lleva lógica de Menu y de sus opciones.
def main():
    os.system('clear') 
    print()
    print('_______________________________________')
    print()
    bus = Bus(int(input('Enter max capacity of the bus: ')))
    print('_______________________________________')
    while True:
        decision = input('''
            What is next?
                        
            Type 1 to Add passenger.
                        
            Type 2 to Remove passenger.

            Type any other key to Exit Program.
            
            Key: ''')
        
        if decision == '1':
            person = Person('one')
            bus.add_passenger(person)
            bus.seats_available()
            
        elif decision == '2':
            bus.remove_passenger()
            bus.seats_available()
        
        else:
            exit()

main()

