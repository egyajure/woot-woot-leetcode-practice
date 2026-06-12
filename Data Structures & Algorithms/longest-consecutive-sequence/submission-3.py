class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_present = set()

        max_length = 0

        for num in nums:
            nums_present.add(num)

        for num in nums:
            if (num - 1) not in nums_present:
                temp = num + 1
                l = 1
                while(temp in nums_present):
                    l += 1
                    temp += 1
                max_length = max(max_length, l)
        
        return max_length

        