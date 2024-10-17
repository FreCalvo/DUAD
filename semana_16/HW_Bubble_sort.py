
#Code for test_HW_Bubble_sort.

def inverse_bubble_sort(list):
    for outer_index in (range(len(list))):
        change_done = False
        for index in reversed(range(len(list))):
            
            current_element = list[index]
            next_element = list[index - 1]
            
            if index >= 1: # If next element reached index -1 (index == 0) program will take last number again as next element.
                if current_element < next_element:
                    list[index] = next_element
                    list[index - 1] = current_element
                    change_done = True

        if not change_done:
            return list
