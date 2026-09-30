class Solution:
    def isValid(self, s: str) -> bool:
        dict = {')':'(', '}':'{', ']':'['}
        stack = []
        for i in range(len(s)):
            if(s[i] in dict.values()):
                stack.append(s[i])
            elif(not stack):
                return False
            elif(dict[s[i]]==stack[-1]):
                stack.pop()
            else:
                return False
        return not stack