class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        if not s.isalnum():
            t=""
            for i in range(len(s)):
                t = t + s[i] if s[i].isalnum() else t
            s = t
        b, e = 0, len(s)-1
        while (e-b)>0:
            if s[b] != s[e]:
                return False
            else:
                b+=1
                e-=1
        return True
