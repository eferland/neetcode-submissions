class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output = output + 'a' + str(len(s)) + 'a' + s
        return output+'b'
    def decode(self, s: str) -> List[str]:
        output = []
        while s[0]=='a':
            end = s[1:].index("a")
            length = int(s[1:end+1])
            output.append(s[end+2:end+2+length])
            s = s[end+2+length:]
        return output
