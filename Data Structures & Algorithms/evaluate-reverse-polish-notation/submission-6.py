class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        so use a stack to store all the current values of the array, and whenever you reach something in there, and it is an operator, use that operator and operate the previous numbers and pop them after

        so 

        stack = []

        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())

            elif i == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)

            elif i == '*':
                stack.append(stack.pop() * stack.pop())

            elif i == '/':
                a,b = float(stack.pop()), float(stack.pop())
                stack.append(b/a)
            
            else:
                stack.append(int(i))
        return stack[0]


        
                

        '''
        stack = []

        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())

            elif i == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)

            elif i == '*':
                stack.append(stack.pop() * stack.pop())

            elif i == '/':
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            
            else:
                stack.append(int(i))
        
        return stack[0]