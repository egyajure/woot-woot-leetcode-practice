class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # the idea is when you find a duplicate string, you shrink left until you get a valid string again

        maxLen = 0

        if (len(s) < 2):
            return len(s)

        l, r = 0, 1
        curChars = set()

        curChars.add(s[l])
        
        while (r < len(s)):
            while(s[r] in curChars):
                curChars.remove(s[l])
                l += 1 
            curChars.add(s[r])
            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen