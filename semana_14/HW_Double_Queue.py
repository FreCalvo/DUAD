class Node:
    data : str

    def __init__(self, data):
        self.data = data
        self.next = None
        

class DoubleQueue:
    def __init__(self):
        self.head = None #Set head as None, so Stack can be created empty and begin adding stuff.
        self.size = 0

    def push_right(self,data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        self.size += 1
        return new_node.data
    

    def pop_right(self):
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        popped_node = current_node.next
        current_node.next = None
        self.size -= 1
        return popped_node.data

                    
        return popped_node.data

    def push_left(self,data):
            new_node = Node(data)
            if self.head is not None:
                new_node.next = self.head
            self.head = new_node
            self.size += 1
            return new_node.data
    
    def pop_left(self):
        try:
            popped_node = self.head
            self.head = self.head.next
            self.size -= 1
            return popped_node.data
        except Exception as error:
            print(f'Array is empty. {error}')
    
    def queue_size(self):
        return self.size

    def print_structure(self):
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

my_queue = DoubleQueue()
print('Adding items with push left.')
print(f'Adding: {my_queue.push_left('Notebook')} to the top of the list.')
print(f'Adding: {my_queue.push_left('Book')} to the top of the list.')
print(f'Adding: {my_queue.push_left('Pen')} to the top of the list.')
print(f'Adding: {my_queue.push_left('Eraser')} to the top of the list.')

print('\nIt is what the structure looks like!')
my_queue.print_structure()
print()
print('Adding one item with push right, it is sent to the bottom.')
print(f'Adding: {my_queue.push_right('laptop')} to the bottom of the list.')

print(f'\nIt is what the structure looks like now!')
my_queue.print_structure()
print('\n Removing item with pop left, it is removed from the top.')
print(my_queue.pop_left())

print(f'\nIt is what the structure looks like now!')
my_queue.print_structure()
print('\n Removing item with pop right, it is removed from the bottom.')
print(my_queue.pop_right())

print(f'\nIt is what the structure looks like now!')
my_queue.print_structure()

print(f'\nQueue size: {my_queue.queue_size()}\n')

