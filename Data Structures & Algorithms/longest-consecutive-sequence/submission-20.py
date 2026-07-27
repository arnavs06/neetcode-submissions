class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
    does not have to be consecutive in the array, so [1,10,2,3,4,5] is 5

    so maybe sorting could work, and then make a counter for the increasing sequence of the numbers starting from the bottom

        so then [1,10,2,3,4,5] -> [1,2,3,4,5,10]

        afterwards, go through the array and add +1 to sequence for any element that is sequentially one greater than the last

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

        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        sequence = 1
        best = 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                sequence += 1
                best = max(best, sequence)
            else:
                sequence = 1
        return best

