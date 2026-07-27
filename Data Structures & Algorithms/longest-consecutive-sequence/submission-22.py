class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        does not have to be consecutive in the array, so [1,10,2,3,4,5] is 5

        so maybe sorting could work, and then make a counter for the increasing sequence of the numbers starting from the bottom

            so then [1,10,2,3,4,5] -> [1,2,3,4,5,10]

            afterwards, go through the array and add +1 to sequence for any increase of the numbers starting from the bottom

            so like

            sequence = 0
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1] - 1:
                    sequence += 1
                else:
                    continue
            return sequence
        '''
        # nums=[2,20,4,10,3,4,5]
        # [2,3,4,5,10,20]

        best = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                best = max(best, length)
        return best

