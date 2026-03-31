class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # basically we want to count if the number of characters in s is equal to t
        # easiest way is to sort both strings and see if they are the same
        # slightly faster would be to make a dict with both and compare, that would be O(n + m)

        sDict = defaultdict(int)

        for char in s:
            sDict[char] += 1
        
        tDict = defaultdict(int)
        for char in t:
            tDict[char] += 1
            if tDict[char] > sDict[char]:
                return False

        return sDict == tDict