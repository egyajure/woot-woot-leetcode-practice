class Solution:
    numDecodingsDict = {}

    def __init__(self):
        self.numDecodingsDict = {}

    # first, top down
    # def numDecodings(self, s: str) -> int:
    #    # we can break this into choices, first two characters or encode just the 1
    #     print(s)
    #     if(len(s) == 0):
    #         return 0
    #     if(s[0] == '0'):
    #         return 0
    #     if(len(s) == 1):
    #         return 1
    #     if (s == "10"):
    #         return 1
    #     if(11<= int(s) <=26):
    #         return 2
    #     if(s in self.numDecodingsDict):
    #         return self.numDecodingsDict[s]
        
    #     if (10 <= int(s[0:2]) <= 26):
    #         num = (self.numDecodings(s[1:]) + self.numDecodings(s[2:]))
    #     else:
    #         num = (self.numDecodings(s[1:]))

    #     self.numDecodingsDict[s] = num
    #     return num
            
    
    # next, bottom up
    def numDecodings(self, s: str) -> int:
        decodings = [0] * len(s)

        if (s[0] == '0'):
            return 0
        if (len(s) == 1):
            return 1
        
        decodings[0] = 1
        decodings[1] = 2 if (10 < int(s[:2]) <= 19 or 20 < int(s[:2]) <= 26) else 1

        for i in range(2, len(s)):
            # print("test", int(s[i-1:i+1]))

            if (s[i] != '0'):
                decodings[i] = decodings[i-1]
            if (10 <= int(s[i-1:i+1]) <= 26):
                decodings[i] += decodings[i-2]
        
        return decodings[len(s) - 1]

        