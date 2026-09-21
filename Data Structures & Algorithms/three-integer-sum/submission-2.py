class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i,k in enumerate(nums):
            if i > 0 and k == nums[i-1]:
                continue
            

            l,r = i+1, len(nums)-1

            while l<r:
                three_sum = nums[l] + nums[r] + k

                if three_sum > 0:
                    r-=1
                elif three_sum < 0:
                    l+=1
                else:
                    ans.append([k ,nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return ans

