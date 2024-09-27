# Analice el algoritmo de bubble_sort usando la Big O Notation.


test_list = [18, -11, 68, 6, 53, 8]

def inverse_bubble_sort(list):

    print(f'Initial list: {list}\n')  # O(1)

    for outer_index in (range(len(list))): # O(n)
        change_done = False # O(1)
        for index in reversed(range(len(list))): # O(n^2)
            
            current_element = list[index]  # O(1)
            next_element = list[index - 1] # O(1)
            
            if index >= 1: # O(1)
                if current_element < next_element: # O(1)
                    list[index] = next_element # O(1)
                    list[index - 1] = current_element # O(1)
                    print(f'{list}') # O(1)
                    change_done = True # O(1)
            else:
                print(f'End of round {outer_index +1}\n') # O(1)

        if not change_done:
            print("No changes in last round. End of iterations. :)") # O(1)
            return # O(1)

inverse_bubble_sort(test_list)