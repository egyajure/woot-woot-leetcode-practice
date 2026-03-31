class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        if (len(s) < 2 or len(s) < k):
            return len(s)

        # my first thought is to find the dominant character as we go
        # ..but instead it makes more sense to zoom out and understand we already know which character will be dominant
        # it will be the most frequent <- Actually we don't :( original more strightforward thought was correct

        # sliding window
        # our target will change continuosly
        l, r = 0, 1
        target_count = 1
        target = s[l]
        frequency = defaultdict(int)
        frequency[s[l]] = 1
        while(r < len(s)):
            frequency[s[r]] += 1
            if (frequency[s[r]] > target_count):
                target = s[r]
            target_count = frequency[target]

            while(r - l + 1 - target_count > k):
                # if (s[l] == target):
                #     target_count -= 1
                frequency[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r-l+1)
            r +=1


        return maxLen
        