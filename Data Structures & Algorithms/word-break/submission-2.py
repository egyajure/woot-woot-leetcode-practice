class Solution:

    canSegment = {}

    def __init__(self):
        self.canSegment = {}

    # first, top down
    # the decision you're making is what word are you removing from the beggining of the string
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if (s in self.canSegment):
            return self.canSegment[s]
        if(len(s) == 0):
            return True
        
        for word in wordDict:
            if (s[:len(word)] == word):
                if (self.wordBreak(s[len(word):], wordDict)):
                    self.canSegment[s[len(word):]] = True
                    return True
                else:
                    self.canSegment[s[len(word):]] = False

        return False
       
        