class MinStack:
    '''
    make 2 stacks, 

    stack = []
    min_stack = []

    whenever you append to the main stack, you append the minimum value of the stack to the min_stack so you have all the minimum values in a min stack

    and if the stack if empty, just append the first value you add to the main stack

    '''
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
