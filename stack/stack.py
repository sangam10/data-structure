# implementation of stack using list
class Stack:
    # initialized constructor
    def __init__(self,stack = list(),max_size=None):
        self.stack = stack
        self.max_size = max_size
    # check if the stack is empty or not
    def is_empty(self):
        return self.size() == 0
    
    # checks if size is full or not
    def is_full(self):
        return self.max_size is not None and self.size() >= self.max_size
    
    # get the size of stack
    def size(self):
        return len(self.stack)

    # push operation
    def push(self,item):
        if self.max_size is None or self.max_size > self.size():
            self.stack.append(item)
        else:
            raise Exception('stack is of full size')
        
    # pop operation
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise Exception('stack is empty')
    
    # read top of stack without pop
    def peek(self):
        if not self.is_empty():
            return self.stack[self.size()-1]
        else:
            raise Exception('stack is empty')

    # get all elements of stack
    def get_stack(self):
        return self.stack.copy()

    # clear the stack
    def clear(self):
        self.stack = list()

    #checks if item is in stack or not
    def contains(self,item):
        return item in self.stack

    #reverse the stack
    def reverse(self):
        return self.stack.reverse()
    
    #copy the stack
    def copy(self):
        return Stack(self.stack.copy())
    

stack = Stack([2,3])
print(stack.get_stack())
print(stack.peek())
print(stack.get_stack())