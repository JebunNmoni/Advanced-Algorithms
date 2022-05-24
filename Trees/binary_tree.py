class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            self._insert(value, self.root)
        else:
            self.root = Node(value)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child:
                self._insert(value, current_node.left_child)
            else:
                current_node.left_child = Node(value)
        elif value > current_node.value:
            if current_node.right_child:
                self._insert(value, current_node.right_child)
            else:
                current_node.right_child = Node(value)
        else:
            print(f'Value {value} already exists.')

    def print_tree(self):
        if self.root:
            self._print_tree(self.root)
        else:
            print('Tree is empty.')

    def _print_tree(self, current_node):
        if current_node:
            self._print_tree(current_node.left_child)
            print(current_node.value)
            self._print_tree(current_node.right_child)

    def depth(self):
        if self.root:
            return self._depth(self.root, 0)
        else:
            return 0
    
    def _depth(self, current_node, current_depth):
        if not current_node: return current_depth
        left_depth = self._depth(current_node.left_child, current_depth+1)
        right_depth = self._depth(current_node.right_child, current_depth+1)
        return max(left_depth, right_depth)

    def search(self, value):
        if not self.root: return False
        return self._search(value, self.root)

    def _search(self, value, current_node):
        if current_node.value == value: return True
        elif value < current_node.value and current_node.left_child:
            return self._search(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child:
            return self._search(value, current_node.right_child)
        return False


def random_fill_tree(tree, num_nodes = 5, max_value = 50):
    from random import randint
    for _ in range(num_nodes):
        tree.insert(randint(0, max_value))
    return tree

binary_serach_tree = random_fill_tree(BST(), num_nodes = 5, max_value = 10000)
binary_serach_tree.insert(15)
binary_serach_tree.insert(10)
binary_serach_tree.print_tree()
print(f'The depth of the tree is {binary_serach_tree.depth()}')

for i in [10, 27, 25, 15]:
    print(f'Value {i} found :: ', binary_serach_tree.search(i))