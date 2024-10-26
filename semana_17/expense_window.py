import PySimpleGUI as sg
import out_functions as l
import data_import_export as d


def add_expense(data_array, file_name, list_categories):
    add_expense_layout = [[sg.Text("Detail:"), sg.Input(key='-DETAIL-', do_not_clear=True, size=(20, 1)), sg.Text(key='-ERROR_1-')],
        [sg.Text("Amount:"), sg.Input(key='-AMOUNT-', do_not_clear=True, size=(10, 1)), sg.Text(key='-ERROR_2-')],
        [sg.Text("Category:"), sg.Input(key='-CATEGORY-', do_not_clear=True, size=(10, 1)), sg.Text(key='-ERROR_3-')],
        [sg.Text("")],
        [sg.Push(), sg.Button('Save'), sg.Button('Back'), sg.Push()]]

    add_expense_window = sg.Window("Add Expense", add_expense_layout)

    while True:
        event, values = add_expense_window.read()
        if event in (sg.WIN_CLOSED, 'Back'):
            break
        elif event == 'Save':
            add_expense_window['-ERROR_1-'].Update('')
            add_expense_window['-ERROR_2-'].Update('')
            add_expense_window['-ERROR_3-'].Update('')
            print(values['-CATEGORY-'])
            print(list_categories)
            
            detail_check = l.check_is_not_blank(values['-DETAIL-'])
            if detail_check == True:
                add_expense_window['-ERROR_1-'].Update(f'Error: Space cannot be left blank!')

            amount_check = l.check_for_number_in_input(values['-AMOUNT-'])
            if amount_check == False:
                add_expense_window['-ERROR_2-'].Update(f'Error: Enter numbers!')

            category_check = l.check_if_category_in_list(list_categories, values['-CATEGORY-'])
            if category_check == False:
                add_expense_window['-ERROR_3-'].Update(f'Error: Category is not listed!')

            if detail_check == False and amount_check == True and category_check == True:
                l.store_information_in_data_list('Expense', values['-DETAIL-'], values['-AMOUNT-'], values['-CATEGORY-'], data_array)

                sg.popup("Information saved!!")
                d.export_data(data_array,file_name)

                add_expense_window['-DETAIL-'].Update('')
                add_expense_window['-AMOUNT-'].Update('')
                add_expense_window['-CATEGORY-'].Update('')

    add_expense_window.close()