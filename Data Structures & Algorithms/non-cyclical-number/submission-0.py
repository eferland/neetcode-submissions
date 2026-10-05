class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            sumsquares = 0
            while n>0:
                sumsquares+=(n%10)**2
                n=n//10
            if sumsquares==1:
                return True
            if sumsquares in seen:
                return False
            seen.add(sumsquares)
            n = sumsquares
    