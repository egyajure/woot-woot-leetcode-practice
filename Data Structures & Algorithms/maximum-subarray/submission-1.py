class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # logic -> if a section is negative, it is not worthwile
        # as in, -a, b will NEVER be better than b
        # similarily, b, c will ALWAYS be better than b

        # ex. 1, 2, -5, 4, 5
        # the longest stretch here is 4, 5 because 1, 2, -5 is -3
        # so greedily we would go 1, 2, -5, oop we've become negative, 1, 2 is the best stretch
        # then 4, oh that's actually better woot woot, 4, 5

        # that is to say I think two pointer would work here

        p = 0

        ans = nums[0]
        temp = 0
        while (p < len(nums)):
            temp += nums[p]
            ans = max(ans, temp)
            if (temp < 0):
                # r just crossed the line
                temp = 0
            p +=1
        
        return ans

        