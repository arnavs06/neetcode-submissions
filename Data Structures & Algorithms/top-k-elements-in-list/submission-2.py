from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        given an array return the k most frequently occuring elements

        maybe using counter? in order to 
        '''

        count = Counter(nums)
        ans = []
        for i, j in count.most_common(k):
            ans.append(i)

        return ans