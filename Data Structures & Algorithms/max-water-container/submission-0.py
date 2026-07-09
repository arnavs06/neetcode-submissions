class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        '''

        use 2 pointers, in order to 
        maximum height is length x width of the 2 bars

        maxArea = 0

        while l > r:

            area = min(heights[l],heights[r]) * (r-l)
            maxArea = max(maxArea, area)

            if heights[l] < heights[r]:
                r-=1
            else:
                l+=1

        return maxArea


        '''
        l,r = 0, len(heights)-1

        maxArea = 0

        while l < r:
            area = min(heights[l],heights[r]) * (r-l)
            maxArea = max(maxArea, area)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return maxArea