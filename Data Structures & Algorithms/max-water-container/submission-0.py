class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l = 0
        r = len(heights)-1
        while l<r:
            best = max(best, (r-l)*min(heights[l], heights[r]))
            if heights[l]< heights[r]:
                l+=1
            else:
                r-=1
        return best
        
        