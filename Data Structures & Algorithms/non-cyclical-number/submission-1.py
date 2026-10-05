class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        dict = {0:0, 1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81}
        while True:
            sumsquares = 0
            while n>0:
                sumsquares+=dict[n%10]
                n=n//10
            if sumsquares==1:
                return True
            if sumsquares in seen:
                return False
            seen.add(sumsquares)
            n = sumsquares
    