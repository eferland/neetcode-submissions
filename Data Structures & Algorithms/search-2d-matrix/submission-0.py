class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        totallength = m*n
        left = 0
        right = totallength-1
        while left <= right:
            mid = (left+right)//2
            mind = mid//n
            nind = mid-(n*mind)
            if(matrix[mind][nind]==target):
                return True
            elif(matrix[mind][nind]<target):
                left = mid+1
            else:
                right = mid-1
        return False