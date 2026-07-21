import math 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        use 2 different passes of the nums array, prefix & postfix, checking all elements before and after a number


        '''
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
        




        








        

            