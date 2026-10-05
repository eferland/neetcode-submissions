class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # use top row and left column as indicators of whether a 0 exists in each row or col
        # Boolean to decide to set first row to 0's
        toprowzero = False
        for j in range(len(matrix[0])):
            if not matrix[0][j]:
                toprowzero = True
                break
        # first pass to set top row/ left col indicators
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # second pass to zeroify
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])-1, -1, -1):
                if not (matrix[i][0] and matrix[0][j]):
                    matrix[i][j] = 0
        # top row check
        if toprowzero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
            

        