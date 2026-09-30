class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        for i in range(len(s)):
            if(s[i]=='(' or s[i]=='{' or s[i]=='['):
                stack += s[i]
            elif(not stack):
                return False
            elif((s[i]==')' and stack[-1]=='(') or (s[i]=='}' and stack[-1]=='{') or (s[i]==']' and stack[-1]=='[')):
                stack = stack[:-1]
            else:
                return False
        return not stack