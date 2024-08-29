

class Student:
    def __init__(self, name, level, spanish, english, history, science):
        self.name = name
        self.level = level
        self.spanish = spanish
        self.english = english
        self.history = history
        self.science = science

    def calculate_average(self):
        return ((self.spanish + self.english + self.history + self.science) / 4)


def check_list(the_list):
    if not the_list:
        raise ValueError('No data. Register at least one student first.')


def get_name():
    try:
        name = str(input("Enter student's full name: "))
    except Exception as error:
        print(f'Error occurred: {error}')
    return name


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


def add_student_to_students_list(students_list,name, level, spanish, english, history, science):
    students_list.append(
        Student(name, level, spanish, english, history, science)
        )
    return students_list


def show_students(students_list):
    print('Students information:')
    print()
    try:
        for student in students_list:
            print(f'''Student
                Name: {student.name}
                Class: {student.level}
                Spanish_score : {student.spanish}
                English_score : {student.english}
                History_score : {student.history}
                Science_score : {student.science}
                ''')
    except: 
                print('No data. Register student.')


# Obtain average per student from CSV.
def get_average_score(student):
    Average = ((int(student.spanish) + int(student.english) + int(student.history) + int(student.science) ) / 4)
    return Average


# Create list with only names and total average per student.
def add_to_averages_list(students_list,averages_list):
    for student in students_list:
        student_average = get_average_score(student)
        name = student.name
        averages_list.append({
            'Full_name' : name,
            'Average' : student_average
    })
    return averages_list


def add_individual_to_averages_list(averages_list, name, individual_average):
    averages_list.append({
            'Full_name' : name,
            'Average' : individual_average
    })


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

def get_total_average(students_list):
    sum_average = 0
    for student in students_list:
        sum_average += get_average_score(student)
    average = sum_average / len(students_list)
    rounded_average = round(average, 2)
    return rounded_average

def exit_system():
    print("See you soon")
    exit()

