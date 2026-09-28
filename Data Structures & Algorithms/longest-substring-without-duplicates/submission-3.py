class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        dict = defaultdict(lambda: -1)
        left = 0
        longest = 1
        for i in range(len(s)):
            if(dict[s[i]]>=left):
                left = dict[s[i]]+1
                dict[s[i]] = i
            else:
                dict[s[i]] = i
                longest = max(longest, i-left+1)
        return longest
