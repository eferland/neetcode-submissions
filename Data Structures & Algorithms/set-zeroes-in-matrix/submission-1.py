class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowindices = set()
        colindices = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    rowindices.add(i)
                    colindices.add(j)
        for row in rowindices:
            matrix[row] = [0]*len(matrix[0])

        for col in colindices:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        