# 3. Cree una clase de `User` que:
#     - Tenga un atributo de `date_of_birth`.
#     - Tenga un property de `age`.
    
#     Luego cree un decorador para funciones que acepten un `User` como parámetro que se 
# encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.

from datetime import date

class User:
    date_of_birth = date

    def __init__(self,date_of_birth):
        self.date_of_birth = date_of_birth
    
    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )

def adults_ony(func):
    def wrapper(user):
        if user.age < 21:
            raise ValueError(
                'User is minor'
            )
        func(user)
    return wrapper

@adults_ony
def grant_access(user):
    print('Your access is granted!')


year = int(input('Enter year of birth(number):\n'))
month = int(input('Enter month of birth(number):\n'))
day = int(input('Enter day of birth(number):\n'))
new_user = User(date(year,month,day))
grant_access(new_user)