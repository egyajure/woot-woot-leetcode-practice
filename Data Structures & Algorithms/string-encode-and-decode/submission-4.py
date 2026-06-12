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
        # while(len(s) > 0):
        #     d = s.find('|')
        #     l = int(s[:d])
        #     s = s[d + 1:]
        #     strings.append(s[:l])
        #     s = s[l:]
        #  ^ finding and copying the string a bunch of times is too slow

        i = 0
        j = 0
        while (i < len(s)):
            # find the deliminator
            j = i
            while (s[j] != '|'):
                j += 1
            
            l = int(s[i:j])

            strings.append(s[j+1: j+l+1])
            i = j+l+1

        return strings
