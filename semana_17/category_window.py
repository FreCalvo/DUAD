import PySimpleGUI as sg
import data_import_export as d
import out_functions as l
import stack as stack

stack_list = []
categories_stack = stack.Stack()


def add_category(list_categories, file_name):    
    
    headings = ["Categories"]
    
    category_window_layout = [
        [sg.Table(values=list_categories, headings=headings, max_col_width=35,
            auto_size_columns=True,
            display_row_numbers=True,
            justification='center',
            num_rows=10,
            enable_events=True,
            key='-INFORMATION_TABLE-',
            row_height=15,
            tooltip='Data Table')],
        [sg.Push(),sg.Text('Enter Category:'),sg.Push()],
        [sg.Push(),sg.Input(key='-CATEGORY-', do_not_clear=True, size=(15,1)),sg.Text(key='-ERROR_1-'), sg.Push()],
        [sg.Push(),sg.Button('Back'),sg.Button('Save'), sg.Push()],
    ]

    category_window = sg.Window("Category", category_window_layout, modal=True)

    while True:
        event, values = category_window.read()
        print(event)
        if event in (sg.WIN_CLOSED, 'Back'):
            break
        elif event == 'Save':
            if l.check_is_not_blank(values['-CATEGORY-']) == True:
                category_window['-ERROR_1-'].Update(f'Error: Space cannot be left blank!')
            else:
                l.store_information_in_category_list(values['-CATEGORY-'], list_categories)

                sg.popup("Information Saved!")
                d.export_data(list_categories,file_name)
                category_window['-INFORMATION_TABLE-'].Update(values=list_categories)
                category_window['-ERROR_1-'].Update(f'')
                category_window['-CATEGORY-'].Update(f'')
    category_window.close()
