# This module has the Menu code only.


def show_header():
    return print('Scores Registration Software')


def display_menu():
    print('Type the number corresponding to the option to do next:')
    print('''
          1. Add new student
          2. Display students info
          3. Display top 3 students
          4. Display total average score
          5. Export Data
          6. Import Data
          7. Exit Menu
          ''')
    
    return input('Option: ')
