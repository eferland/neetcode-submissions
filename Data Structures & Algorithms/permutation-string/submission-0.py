class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False
        s1count = [0]*26
        for i in range(len(s1)):
            s1count[ord(s1[i])-97]+=1
        left, right = 0, 0
        s2count = [0]*26
        while right<len(s1):
            s2count[ord(s2[right])-97]+=1
            right+=1
        right-=1
        while right<len(s2)-1:
            if(s1count == s2count):
                return True
            else:
                right+=1
                s2count[ord(s2[right])-97]+=1
                s2count[ord(s2[left])-97]-=1
                left+=1
        return s1count==s2count



        