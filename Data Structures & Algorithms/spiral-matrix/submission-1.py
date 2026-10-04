class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n
        top = 0
        bottom = m
        output = []
        while len(output)<m*n:
            # append outer layer to output
            # top row
            for i in range(left,right):
                output.append(matrix[top][i])
            # right col
            for i in range(top+1, bottom-1):
                output.append(matrix[i][right-1])
            # bottom row
            if(bottom!=top+1):
                for i in range(right-1, left-1, -1):
                    output.append(matrix[bottom-1][i])
            # left col
            if(left!=right-1):
                for i in range(bottom-2, top, -1):
                    output.append(matrix[i][left])
            left +=1
            right -= 1
            top+=1
            bottom-=1
        return output
