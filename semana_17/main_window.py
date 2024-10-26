import PySimpleGUI as sg
import expense_window as e
import income_window as i
import category_window as c
import out_functions as l


def main_window():
    file_data = 'data.csv'
    data_array = []
    # d.import_data(file_data, data_array)
    file_categories = 'categories.csv'
    list_categories = []

    l.update_content(file_data, data_array)
    l.update_content(file_categories, list_categories)

    headings = ["Type","Detail", "Amount","Category"]
    
    sg.theme("LightBrown1")

    main_window_layout = [
        [sg.Push(),sg.Button('Add Category'), sg.Button('Add Expense'), sg.Button('Add Income'),sg.Push()],
        [sg.HorizontalSeparator(color='white')],
        [sg.Text()],
        [sg.Table(values=data_array, headings=headings, max_col_width=35,
            auto_size_columns=True,
            display_row_numbers=True,
            justification='center',
            num_rows=10,
            enable_events=True,
            key='-INFORMATION_TABLE-',
            row_height=15,
            tooltip='Data Table')],
            [sg.Push(), sg.Button('Update table'), sg.Text(key='-ERROR_1-'), sg.Push()],
    ]

    main_window = sg.Window("Finance tracker", main_window_layout)

    while True:
        event, values = main_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Add Category':
            c.add_category(list_categories, file_categories)
        elif event == 'Add Expense':
            main_window['-ERROR_1-'].Update(f'')
            e.add_expense(data_array, file_data, list_categories)
        elif event == 'Add Income':
            main_window['-ERROR_1-'].Update(f'')
            i.add_income(data_array, file_data, list_categories)
        elif event == 'Update table':
            if data_array == []:
                main_window['-ERROR_1-'].Update(f'Data file is empty. Proceed to add expense or income')

            else:
                print(data_array)
                main_window['-INFORMATION_TABLE-'].Update(values=data_array)
main_window()
