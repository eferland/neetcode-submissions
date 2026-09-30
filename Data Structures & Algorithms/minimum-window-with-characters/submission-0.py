class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(len(t)>len(s)):
            return ""
        scount, tcount = defaultdict(int), defaultdict(int)
        for i in range(len(t)):
            scount[s[i]]+=1
            tcount[t[i]]+=1
        minsubstring = s
        left = 0
        right = len(t)-1
        goalmatches = len(tcount.keys())
        currmatches = 0
        for key in tcount.keys():
            if(scount[key]>=tcount[key]):
                currmatches+=1
        foundmatch = False
        while right<len(s):
            # shrink current window from left as much as possible
            while currmatches == goalmatches:
                foundmatch=True
                scount[s[left]]-=1
                # losing leftmost character causes window to not include t
                if scount[s[left]]<tcount[s[left]]:
                    currmatches-=1
                    if right-left+1<len(minsubstring):
                        minsubstring = s[left:right+1]
                left+=1

            # widen window to get containment
            while currmatches<goalmatches:
                # unable to find more matching windows
                if right+1 == len(s):
                    break
                else:
                    right+=1
                    scount[s[right]]+=1
                    if(scount[s[right]]==tcount[s[right]]):
                        currmatches+=1
            else:
                continue
            
            break
        if foundmatch:
            return minsubstring
        else:
            return ""




