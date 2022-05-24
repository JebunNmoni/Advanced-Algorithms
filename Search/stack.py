class Node(object):
    def __init__(self, x):
        self.data = x
        self.next = None

class Stack(object):
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self, x):
        new_node = Node(x)

        if self.top:
            new_node.next = self.top
        self.top = new_node

        self.size +=1

    def pop(self):
        if not self.top:
            return None
        result = self.top
        self.top = result.next
        self.size -= 1
        return result

    def peek(self):
        if not self.top:
            return None
        return self.top.data
    
    def print_stack(self):
        if not self.top:
            print('Stack is empty.')
        else:
            print('Following is how the stack looks.')
            current_node = self.top
            while current_node:
                offset_str = len(str(current_node.data))
                left_offset = (25 - offset_str) // 2
                right_offset = 25 - offset_str - left_offset
                print('|'+' '*(left_offset-1)+ str(current_node.data)+ ' '*(right_offset-1) +'|')
                print('='*(left_offset+offset_str+right_offset))
                current_node = current_node.next

    def is_empty(self):
        return self.top == None
    
    def stack_size(self):
        return self.size


stk = Stack()
stk.push(5)
stk.push(65)
stk.push(7)
stk.push(8808)
stk.push(9)
stk.push('dog')
stk.push('cat')
stk.push('mouse')
stk.push([1, 3])
stk.print_stack()

print('Peek the top value :: ', stk.peek())
print('Popping two elements')
for i in range(2):
    stk.pop()
stk.print_stack()
print('Popping more than number of elements')
for i in range(200):
    stk.pop()
print('Stack is empty :: ',stk.is_empty())
print('Stack size is :: ', stk.stack_size())
stk.print_stack()
print('Pushing new elements')
stk.push(35)
stk.push(90)
stk.print_stack()
print('Stack size is :: ', stk.stack_size())
