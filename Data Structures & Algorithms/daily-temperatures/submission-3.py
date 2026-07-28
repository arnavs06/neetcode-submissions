class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        use a stack to store the streak of days that are colder until the next warmer day

        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]
            index = stack.pop()
            ans[index] = i - index
        stack.append(i)
        
        return ans


        use a stack to store indices of days that haven't found a warmer day yet, and when you hit a warmer day, 
        pop from the stack and the answer for that index is just the difference between the current index and 
        the popped index
        
        '''
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        
        return ans

