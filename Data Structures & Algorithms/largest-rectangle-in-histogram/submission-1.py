class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftboundaries = [0]*len(heights)
        rightboundaries = [0]*len(heights)
        lstack = []
        rstack = []
        for i in range(len(heights)):
            # finding leftboundaries
            while lstack and heights[lstack[-1]]>=heights[i]:
                lstack.pop()
            leftboundaries[i] = -1 if not lstack else lstack[-1]
            lstack.append(i)
            # finding right boundaries
            while rstack and heights[rstack[-1]]>=heights[len(heights)-i-1]:
                rstack.pop()
            rightboundaries[len(heights)-i-1] = len(heights) if not rstack else rstack[-1]
            rstack.append(len(heights)-i-1)
        # get best area
        best = 0
        for i in range(len(heights)):
            best = max(best, heights[i]*(rightboundaries[i]-leftboundaries[i]-1))
        return best
