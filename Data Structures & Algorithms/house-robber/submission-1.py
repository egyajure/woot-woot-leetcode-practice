class Solution:
    houses = {}

    def __init__(self):
        self.houses = {}

    # first, top down (recursive)
    def rob(self, nums: List[int]) -> int:
        # top down is basically about the choice you make
        # at every point you can either rob the current house or the previous house

        if (len(nums) == 0):
            return 0
        if (len(nums) == 1):
            return nums[0]
        if (len(nums) in self.houses):
            return self.houses[len(nums)]
        
        maxRob = max(nums[len(nums) - 1] + self.rob(nums[:-2]), self.rob(nums[:-1]))
        self.houses[len(nums)] = maxRob
        return maxRob
        