class Solution:
    def charset(self, s: str) -> Tuple:
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in range(len(strs)):
            if self.charset(strs[i]) in dictionary:
                dictionary[self.charset(strs[i])].append(strs[i])
            else:
                dictionary[self.charset(strs[i])] = [strs[i]]
        return list(dictionary.values())
