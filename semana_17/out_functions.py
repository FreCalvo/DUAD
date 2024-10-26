import data_import_export as d

def check_if_category_in_list(nested_list, word_to_check):

    if any(word_to_check in sublist for sublist in nested_list):
        return True 
    else:
        return False
    
def check_for_number_in_input(input_to_check):
    return input_to_check.isdigit()

def check_is_not_blank(input_to_check):
    if input_to_check == '':
        return True
    else:
        return False

def update_content(file_name, data):
    d.import_data(file_name, data)

def store_information_in_category_list(values, list_to_append):
    info_to_append = [values]
    list_to_append.append(info_to_append)
    print(list_to_append)

def store_information_in_data_list(income_expense, detail, amount, category, list_to_append):
    info_to_append = [income_expense, detail, amount, category]
    list_to_append.append(info_to_append)
    print(list_to_append)