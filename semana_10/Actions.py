# This module has the code for the Menu actions.
import os
import csv

def read_csv_or_empty_list(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
    else:
        data = []
    return data


def check_list(the_list):
    if not the_list:
        raise ValueError('No data. Register at least one student first.')


def get_name():
    try:
        name = str(input("Enter student's full name: "))
    except Exception as error:
        print(f'Error occurred: {error}')
    return name


# Get class.
def get_level():
    try:
        level = str(input("Enter student's class: "))
    except Exception as error:
        print(f'Error occurred: {error}')
    return level


def get_subject_score(subject):
    while True:
            try:
                subject = int(input(f'Enter {subject} score: '))
                if subject > 0 and not subject > 100 :
                    return subject
                else:
                    print('Number must be between 0 and 100')
            except Exception as error:
                print(f'Error occurred: {error}')


# Add student info in the main list.
def add_student_to_students_list(students_list, name, level, spanish, english, history, science):
    students_list.append({
        'Full_name' : name,
        'Class' : level,
        'Spanish_score' : spanish,
        'English_score' : english,
        'History_score' : history,
        'Science_score' : science,
    })
    return students_list


# Obtain average per student from CSV.
def get_average_score(scores):
    Average = ((int(scores['Spanish_score']) + int(scores['English_score']) + int(scores['English_score']) + int(scores['Science_score']) ) / 4)
    # print(average)
    return Average


#Obtain average per student when registered the first time.
def get_individual_average(spanish, english, history, science):
    individual_average = ((spanish+english+history+science)/4)
    return individual_average


def add_individual_to_averages_list(averages_list, name, individual_average):
    averages_list.append({
            'Full_name' : name,
            'Average' : individual_average
    })

# Display whole list of students with each of their scores.
def show_students(students_list):
    print('Students information:')
    print()
    try:
        for student in students_list:
            print(f'''Student
                Name: {student['Full_name']}
                Class: {student['Class']}
                Spanish_score : {student['Spanish_score']}
                English_score : {student['English_score']}
                History_score : {student['History_score']}
                Science_score : {student['Science_score']}
                ''')
    except: 
                print('No data. Register student.')

# Create list with only names and total average per student.
def add_to_averages_list(students_list,averages_list):
    for student in students_list:
        student_average = get_average_score(student)
        name = student['Full_name']
        averages_list.append({
            'Full_name' : name,
            'Average' : student_average
    })
    return averages_list


def find_top_3(data):
    sorted_data = sorted(data, key=lambda x: x['Average'], reverse=True)
    return sorted_data[:3]


def show_top_3(list_top_3):
    print('List Top 3')
    print()
    student_number = 1
    for student in list_top_3:
        print(f'''Student # {student_number}
            Name: {student['Full_name']}
            Average: {student['Average']}
            ''')
        student_number += 1


# Function to have total average.
def get_total_average(students_list):
    sum_average = 0
    for student in students_list:
        student['average'] = get_average_score(student)
        sum_average = sum_average + student['average']
        average = sum_average/(len(students_list))
        rounded_average = round(average, 2)
    return rounded_average


# Exit Menu.
def exit_system():
    print("See you soon")
    exit()