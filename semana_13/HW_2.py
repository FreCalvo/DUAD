# Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore 
# son números, y arroje una excepción de no ser así.


# Decorator function.
def numbers_only(func):
    def wrapper(*args):
        for param in args:
            if not isinstance(param,(int,float)): # isinstance verifies parameters are either int or float types.
                    raise ValueError(
                        'Check parameter values, all must be numbers'
                    )
        func(*args)
    return wrapper



@numbers_only
def display_batch_sizes(*args):
    print(f'Batch sizes for today: {args}')


display_batch_sizes(2000,1056,501)