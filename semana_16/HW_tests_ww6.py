# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def prime_number(numbers_list):
    prime_list = []
    index = 0
    for index, num in enumerate(numbers_list):
        x = num -1
        while (x >1):
            if num % x == 0:
                break
            x = x -1
            index +=1   
        else:
            prime_list.append(num)
    for i in range(len(prime_list)-1,-1, -1):
        if prime_list[i] == 1:
            prime_list.pop(i)
    return prime_list


# Cree una función que acepte un string con palabras separadas por un guión y retorne un string 
# igual pero ordenado alfabéticamente.
def order_str(string):
    str_list = []
    separator = '-'
    str_list = string.split(separator)
    alph_list = sorted(str_list)
    final_str = separator.join(alph_list)
    return  final_str


#Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
def count_upper_lower_cases(str):
    upper = 0
    lower = 0
    index = 0
    
    for letter in str:
        if letter.isupper():
            upper += 1
            index += 1
        elif letter.islower():
            lower += 1
            index += 1

    return (f'Upper = {upper}. Lower = {lower}')
