# This is the Main module. Links all the modules.

import os
import time
import Menu as m
import Actions as a
import Data as d

def main():
    os.system('clear')
    averages_list = []
    file_name = 'Students_records.csv'
    students_list = a.read_csv_or_empty_list(file_name)
    a.add_to_averages_list(students_list,averages_list)
    top_3 = a.find_top_3(averages_list)

    while True: 
        print()
        m.show_header()
        print('------------------------------------------------------------')
        option = m.display_menu()
        print()

        if (option == '1'):
            name = a.get_name()
            level = a.get_level()
            spanish_score = a.get_subject_score('Spanish')
            english_score = a.get_subject_score('English')
            history_score = a.get_subject_score('History')
            science_score = a.get_subject_score('Science')
            a.add_student_to_students_list(students_list, name, level, spanish_score, english_score, history_score,science_score)
            individual_average = a.get_individual_average(spanish_score, english_score, history_score, science_score)
            a.add_individual_to_averages_list(averages_list, name, individual_average)
            print('Student registered correctly.')
            print()
            top_3 = a.find_top_3(averages_list)
            time.sleep (1.5)

        elif (option == '2'):
            try:
                a.check_list(students_list)
                a.show_students(students_list)
            except ValueError as error:
                print(error)
            time.sleep (1.5)

        elif (option == '3'):
            try:
                a.check_list(top_3)
                a.show_top_3(top_3)
            except ValueError as error:
                print(error)    
            time.sleep (2)

        elif (option == '4'):
            try:
                print('Total average is:')
                print(a.get_total_average(students_list))
            except:
                print('No data. Register at least one student first.')
                print()
            time.sleep (2)
        
        elif (option == '5'):   
            try:
                d.write_file(file_name,students_list, students_list[0].keys())
                print('Data successfully exported.')
                print()
            except: 
                print('There are no records to export. Register at least one student first.')
            time.sleep (2)

        elif (option == '6'):  
            print()
            try:
                imported_list = d.import_file(file_name)
                a.show_students(imported_list)
                print(f'Data successfully imported.')
                print()
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