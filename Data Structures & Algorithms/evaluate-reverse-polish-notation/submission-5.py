class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opdict = {"+": lambda x,y: x+y, "-": lambda x,y: x-y, "*": lambda x, y: x*y, "/": lambda x,y: int(x/y)}
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in opdict.keys():
                right = stack.pop()
                left = stack.pop()
                stack.append(opdict[tokens[i]](left, right))
            else:
                stack.append(int(tokens[i]))
        return stack.pop()

