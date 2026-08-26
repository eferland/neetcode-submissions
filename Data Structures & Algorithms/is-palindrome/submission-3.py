class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
        b, e = 0, len(s)-1
        while not s[b].isalnum() and b!=len(s)-1:
            b+=1
        while not s[e].isalnum() and e!=0:
            e-=1
        while (e-b)>0:
            if s[b].lower() != s[e].lower():
                return False
            else:
                b+=1
                e-=1
                while not s[b].isalnum() and b!=len(s)-1:
                    b+=1
                while not s[e].isalnum() and e!=0:
                    e-=1
        return True