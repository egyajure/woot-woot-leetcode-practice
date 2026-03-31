class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # i think we grow until the leftmost character isn't needed

        tDict = defaultdict(int)
        for c in t:
            tDict[c] += 1
        
        sDict = defaultdict(int)

        l, r = 0, 0

        minLen = len(s)
        start, end = -1, -1

        while (r < len(s)):
            sDict[s[r]] += 1

            while (l< len(s) and sDict[s[l]] > tDict[s[l]]):
                sDict[s[l]] -= 1
                l += 1
            
            matches = True
            for key, val in tDict.items():
                if sDict[key] < val:
                    matches = False
                    break


            if (matches and minLen >= r-l + 1):
                minLen = r-l+1
                start = l
                end = r
            
            r += 1

        if (start == -1):
            return ""
        return s[start:end+1]
        