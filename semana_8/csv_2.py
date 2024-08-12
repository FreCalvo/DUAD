# Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
# Debe incluir:
#   Nombre
#   Género
    # Desarrollador
    # Clasificación ESRB

# Ejemplo de archivo final:

# nombre,genero,desarrollador,clasificacion
# Grand Theft Auto IV,Accion,Rockstar Games,M
# The Elder Scrolls IV: Oblivion,RPG,Bethesda,M
# Tony Hawk's Pro Skater 2,Deportes,Activision,T

#_______________________________________________________________

# Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.
# Ejemplo de archivo final:

# nombre	genero	desarrollador	clasificacion
# Grand Theft Auto IV	Accion	Rockstar Games	M
# The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
# Tony Hawk's Pro Skater 2	Deportes	Activision	T


#Imports.
import csv
import time
import os

#Frase inicial.
def initial_message():
    print('Video Games Repository')


#Solicito al usuario que digite cantidad de juegos a guardar.
def get_quantity_games():
    while True:
        try:
            count_games = int(input('Enter quantity of games you want to register: '))
            return count_games
        except Exception as error:
            print(f'Error: number needed. {error}')


#Ingreso de información a la lista de dicts.
def add_to_dict(games_list, count, count_games):
    while count < count_games:
        games_list.append({
            'Name' : input(f'Enter Name: '),
            'Type' : input(f'Enter Type: '),
            'Developer' : input(f'Enter Developer: '),
            'Classification' : input(f'Enter Classification: '),
        })
        count +=1
        time.sleep(1)
    print(games_list)


#Escritura en CSV.
def write_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers, delimiter= '\t')
        writer.writeheader()
        writer.writerows(data)


#Func Main para definir lista inicial, count y ejecición de funciones.
def main ():
    games_list = []
    count = 0
    initial_message()
    add_to_dict(games_list, count, get_quantity_games())
    write_file('Games_info_tabs.csv', games_list, games_list[0].keys())


#Ejecución de Main.
if __name__ == "__main__":
  os.system('clear')
  main()