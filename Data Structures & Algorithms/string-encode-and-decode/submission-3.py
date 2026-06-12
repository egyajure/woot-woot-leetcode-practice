class Solution:

    def encode(self, strs: List[str]) -> str:
        # length + deliminator + string
        encoded = ""

        for s in strs:
            encoded += str(len(s))
            encoded += "|"
            encoded += s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        strings = []
        while(len(s) > 0):
            d = s.find('|')
            l = int(s[:d])
            s = s[d + 1:]
            strings.append(s[:l])
            s = s[l:]

        return strings
