class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # reflect across positive diagonal
        for i in range(n):
            for j in range(n-1-i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
        # then reflect across horizontal midline
        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]