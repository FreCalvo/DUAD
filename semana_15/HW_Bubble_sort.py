# Crea un bubble_sort por tu cuenta sin revisar el código de la lección.
# Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).

# Este hace lo mismo que el resto, solo que recorre la lista de derecha a izquierda, y las “burbujas” son los elementos menores, no los mayores.


def inverse_bubble_sort(list):

    print(f'Initial list: {list}\n')

    for outer_index in (range(len(list))):
        change_done = False
        for index in reversed(range(len(list))):
            
            current_element = list[index]
            next_element = list[index - 1]
            
            if index >= 1: # If next element reached index -1 (index == 0) program will take last number again as next element.
                if current_element < next_element:
                    list[index] = next_element
                    list[index - 1] = current_element
                    print(f'{list}')
                    change_done = True
            else:
                print(f'End of round {outer_index +1}\n')

        if not change_done:
            print("No changes in last round. End of iterations. :)")
            return

test_list = [18, -11, 68, 6, 53, 8]
inverse_bubble_sort(test_list)
