class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # order isn't relevant, cannot sort
        # So probably nothing to do with left/right pointers or stacks or clever traversal

        numbers = set(nums) # we only care about if there is one of each, duplicates don't help
        max_length = 0

        for num in numbers:
            length = 1
            while num + length in numbers:
                length +=1
            max_length = max(max_length, length)
        
        return max_length
        