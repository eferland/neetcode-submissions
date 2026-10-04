class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = n-1
        t = 1
        b = m-1
        movementdir = 0
        output = []
        i = 0
        j = 0
        while len(output)<m*n:
            output.append(matrix[i][j])
            # moving right
            if movementdir==0:
                if j==r:
                    r-=1
                    movementdir = (movementdir+1)%4
                    i+=1
                else:
                    j+=1
            # moving down
            elif movementdir==1:
                if i==b:
                    b-=1
                    movementdir = (movementdir+1)%4
                    j-=1
                else:
                    i+=1
            # moving left
            elif movementdir==2:
                if j==l:
                    l+=1
                    movementdir = (movementdir+1)%4
                    i-=1
                else:
                    j-=1
            # moving up
            else:
                if i==t:
                    t+=1
                    movementdir = (movementdir+1)%4
                    j+=1
                else:
                    i-=1
        return output

