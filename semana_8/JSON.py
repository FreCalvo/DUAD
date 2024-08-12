#Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
#     1. Debe leer el archivo para importar los Pokémones existentes.
#     2. Luego debe pedir la información del Pokémon a agregar.
#     3. Finalmente debe guardar el nuevo Pokémon en el archivo.



import os
import json

#Abrir arcjivo JSON.
def open_file(file_path):
    with open(file_path) as file:
        data = json.load(file)
        return data


#Agregar nuevo pokemon al Dict.
def new_item(new_pokemon, data):
    name = input("Enter pokemon's name: ")
    new_pokemon['name'] = {'English' : name}
    types = input ("Enter pokemon's type: ")
    new_pokemon['type'] = [types]
    new_pokemon ['base'] = {}
    bases = [ 'HP', 'Attack', 'Defense', 'Sp.Attack', 'Sp. Defense', 'Speed']
    for base in bases:
        value = int(input(f"Enter pokemon's {base}: "))
        new_pokemon['base'][base] = value
    data.append(new_pokemon)


#Escribir Dict en archivo.
def write_file (file_path, data):
    with open(file_path,'w') as f:
        json.dump(data, f, indent=2)


def main():
    count = 0
    new_pokemon = {}
    
    with open('pokemon.json') as file:
        data = json.load(file)
    new_item(new_pokemon, data)
    write_file('pokemon.json',data)



if __name__ == "__main__":
    os.system('clear')
    main()