from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        given an array return the k most frequently occuring elements

        maybe using counter? 

        so first create a hashmap with counter, and then the result array to append the results
        using that hashmap and use the most_common() function inside of Counter to return the K frequent elements

        Time complexity : O(nlogn) with most_common and how it sorts
        '''

        count = Counter(nums)
        ans = []
        for i, j in count.most_common(k):
            ans.append(i)

        return ans