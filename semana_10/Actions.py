# This module has the code for the Menu actions.

# Get student's name.
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


# Get Spanish score.
def get_spanish():
    while True:
        try:
            spanish = int(input("Enter Spanish score: "))
            if spanish > 0 and not spanish > 100 :
                return spanish
            else:
                print('Number must be between 0 and 100')
        except Exception as error:
            print(f'Error occurred: {error}')
        

# Get English score.
def get_english():
    while True:
        try:
            english = int(input("Enter English score: "))
            if english > 0 and not english > 100 :
                return english
            else:
                print('Number must be between 0 and 100')
        except Exception as error:
            print(f'Error occurred: {error}')


# Get History score.
def get_history():
    while True:
        try:
            history = int(input("Enter History score: "))
            if history > 0 and not history > 100 :
                return history
            else:
                print('Number must be between 0 and 100')
        except Exception as error:
            print(f'Error occurred: {error}')


# Get Science score.
def get_science():
    while True:
        try:
            science = int(input("Enter Science score: "))
            if science > 0 and not science > 100 :
                return science
            else:
                print('Number must be between 0 and 100')
        except Exception as error:
            print(f'Error occurred: {error}')


# Add student info in the main list.
def add_to_list(students_list, name, level, spanish, english, history, science):
    students_list.append({
        'Full_name' : name,
        'Class' : level,
        'Spanish_score' : spanish,
        'English_score' : english,
        'History_score' : history,
        'Science_score' : science,
    })
    return students_list


# Obtain average per student.
def get_average_score(scores):
    return ((scores['Spanish_score'] + scores['English_score'] + scores['English_score'] + scores['Science_score'] ) / 4)


# Create list with only names and total average per student.
def add_averages_list(students_list,averages_list):
    for student in students_list:
        student_average = get_average_score(student)
        name = student['Full_name']
    averages_list.append({
        'Full_name' : name,
        'Average' : student_average
    })
    return averages_list


# Display whole list of students with each of their scores.
def show_students(students_list):
    print('Students information')
    print()
    for student in students_list:
        print(f'''Student
            Name: {student['Full_name']}
            Class: {student['Class']}
            Spanish_score : {student['Spanish_score']}
            English_score : {student['English_score']}
            History_score : {student['History_score']}
            Science_score : {student['Science_score']}
            ''')


# Find top 3.
def find_top_3(data):
    sorted_data = sorted(data, key=lambda x: x['Average'], reverse=True)
    return sorted_data[:3]


# Display top 3.
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
    return average


# Exit Menu.
def exit_system():
    print("See you soon")
    exit()