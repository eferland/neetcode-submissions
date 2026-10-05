class Solution:
    def myPow(self, x: float, n: int) -> float:
        # repeated squaring method
        if not n:
            return 1
        if n<0:
            x=1/x
            n = -1*n
        instructions = format(n, 'b')
        res=1
        for i in range(len(instructions)):
            res*=res
            if instructions[i]=='1':
                res*=x
        return res

