class Node:
    data : str

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None #Set head as None, so Stack can be created empty to begin adding stuff.
        self.size = 0
    
    def push(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        print(new_node.data)
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.data
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.head.data
    
    def is_empty(self):
        return self.size == 0
    
    def stack_size(self):
        return self.size
    
    def print_structure(self):
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next



my_stack = Stack()
# Stack 3 objects
my_stack.push('notebook')
my_stack.push('book')
my_stack.push('headset')

# Print structure.
print('\nThis is the stack structure:')
my_stack.print_structure()

# Run pop, peek, empty and size methods
print('\nData modifications:')
print(f'Pop: {my_stack.pop()}')
print(f'Pop: {my_stack.pop()}')

print('\nData information:')
print(f'Peek: {my_stack.peek()}')
print(f'Is empty: {my_stack.is_empty()}')
print(f'Size: {my_stack.stack_size()}')

print('\nThis is the stack structure:')
my_stack.print_structure()