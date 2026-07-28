class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        use a stack to store the streak of days that are colder until the next warmer day

        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)-1):
            while stack and temperatures[i] > temperatures[stack[-1]]
            index = stack.pop()
            ans[index] = i - index
            stack.append(i)
        
        return ans
        
        '''
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        
        return ans

