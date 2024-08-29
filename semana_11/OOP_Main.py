# This is the Main module. Links all the modules.

import os
import time
import OOP_Menu as m
import OOP_Actions as a
import OOP_Data as d

def main():
    os.system('clear')
    averages_list = []
    students_list = []
    file_name = 'Students_records.csv'
    students_list = d.read_csv_to_objects(file_name)
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
            spanish = a.get_subject_score('Spanish')
            english = a.get_subject_score('English')
            history = a.get_subject_score('History')
            science = a.get_subject_score('Science')
            student = a.Student(name,level,spanish,english,history,science)
            a.add_student_to_students_list(students_list,name, level, spanish, english, history, science)
            individual_average = student.calculate_average()
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
                dicts = d.objects_to_dicts(students_list)
                d.write_dicts_to_csv(dicts, file_name)
                print('Data successfully exported.')
                print()
            except: 
                print('There are no records to export. Register at least one student first.')
            time.sleep (2)

        elif (option == '6'):  
            print()
            imported_data = d.read_csv_to_objects(file_name)
            if imported_data == []:
                print('No file created yet.')
                continue
            a.show_students(imported_data)
            print(f'Data successfully imported.')
            print()


        elif (option == '7'):
            a.exit_system()

        else:
            print('Not valid: choose option from the Menu')
            time.sleep(2.5)
            print('')

main()