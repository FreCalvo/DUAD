# This is the Main module. Links all the modules.

import os
import time
import Menu as m
import Actions as a
import Data as d



def main():
    os.system('clear')
    students_list = []
    averages_list = []

    while True: 
        print(m.show_header())
        # NONE
        print('------------------------------------------------------------')
        option = m.display_menu()
        print('')

        if (option == '1'):
            name = a.get_name()
            level = a.get_level()
            spanish_score = a.get_spanish()
            english_score = a.get_english()
            history_score = a.get_history()
            science_score = a.get_science()
            a.add_to_list(students_list, name, level, spanish_score, english_score, history_score,science_score)
            print('Student registered correctly')
            print('')
            data = a.add_averages_list(students_list,averages_list)
            top_3 = a.find_top_3(data)
            time.sleep (1.5)

        elif (option == '2'):
            try:
                print(a.show_students(students_list))
            except: 
                print('No data. Register student.')
            time.sleep (2)

        elif (option == '3'):
            try:
                print(a.show_top_3(top_3))
            except:
                print('No data. Register student.')
            time.sleep (2)

        elif (option == '4'):
            try:
                print('Total average is:')
                print(a.get_total_average(students_list))
            except:
                print('No records yet, enter data.')
                print()
            time.sleep (2)
        
        elif (option == '5'):   
            try:
                d.write_file('Students_records.csv',students_list, students_list[0].keys())
            except: 
                print('There are no records to export. Register at least one student first.')
            time.sleep (2)

        elif (option == '6'):  
            try:
                d.read_file('Students_records.csv')
            except:
                print('No file created yet.')
                print()  
            time.sleep (2)  

        elif (option == '7'):
            a.exit_system()

        else:
            print('Not valid: choose option from the Menu')
            time.sleep(2.5)
            print('')


main()