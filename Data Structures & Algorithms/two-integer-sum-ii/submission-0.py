class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        two sum but in O(1) space

        two pointer sol, where you just check if l+r = target, if too small, move left pointer ro the right, and vice versa


        '''

        l,r = 0, len(numbers) - 1

        while l<=r:
            if numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                return [l+1, r+1]

        