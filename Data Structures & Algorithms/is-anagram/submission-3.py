class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Create a hashmap for s and t
        mapS = {}
        mapT = {}

        # iterate through s and count the occurrences of each character
        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)

        # now make sure each character count in s and t is the same
        for c in mapS:
            if mapS[c] != mapT.get(c, 0):
                return False

        return True 