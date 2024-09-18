
class Node:
    def __init__(self, value):
        self.value = value # Each node has two children. Left child is a smaller value, the right child is a larger value.
        self.left_child = None # Pointer for the left child
        self.right_child = None # Pointer for the right child


class BinaryTree:
    def __init__(self):
        self.root = None # it is None because when we are firstly setting up the tree there won´t be any root

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root) # _insert function is going to be recursive.
    
    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print('Value already exists in the tree.')
    
    def print_tree_structure(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

    def height_of_tree(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0
        
    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)


tree = BinaryTree()

tree.insert(4)
tree.insert(5)
tree.insert(8)
tree.insert(1)
tree.insert(9)
tree.insert(12)
tree.insert(14)
tree.insert(11)
tree.insert(0)
tree.insert(99)

print('The current structure is:')
tree.print_tree_structure()

print((f'Tree height is: {tree.height_of_tree()}'))

