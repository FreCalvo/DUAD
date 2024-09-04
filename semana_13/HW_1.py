# Cree un decorador que haga print de los parámetros y retorno de la función que decore.

class Machine:
    status_on: bool

    def __init__(self,status_on):
        self.status_on = status_on


def on_only(func):
    def wrapper(status, **kwargs):
        #Extra logic before function execution.
        print(f'Status ON: {status.status_on}')
        for num, param in enumerate (kwargs.keys()): #Here only take the keys to enumerate variables names present in the machine.
            print(f'Variable {num+1}: {param}')

        if status.status_on != True:
            raise ValueError('Machine is not ON')
        #Function execution
        func(status, **kwargs)
        #No extra logic after function execution in this case.
    return wrapper

@on_only
def check_parameters(status, **kwargs):
    print(f'Current parameters are: {kwargs}')

machine1 = Machine(True)
check_parameters(machine1,Temperature = 200, Pressure = 90, Gas_flow = 45)