class Solution:
    houses = {}

    def __init__(self):
        self.houses = {}

    # first, top down (recursive)
    # def rob(self, nums: List[int]) -> int:
    #     # top down is basically about the choice you make
    #     # at every point you can either rob the current house or the previous house

    #     if (len(nums) == 0):
    #         return 0
    #     if (len(nums) == 1):
    #         return nums[0]
    #     if (len(nums) in self.houses):
    #         return self.houses[len(nums)]
        
    #     maxRob = max(nums[len(nums) - 1] + self.rob(nums[:-2]), self.rob(nums[:-1]))
    #     self.houses[len(nums)] = maxRob
    #     return maxRob
    

    # next, bottom up (iterative)
    def rob(self, nums: List[int]) -> int:
        # iterative is basically taking advantage of those base cases and starting with them instead of ending with them
        
        if (len(nums) == 0):
            return 0
        if (len(nums) == 1):
            return nums[0]
        
        maxRob = [0] * (len(nums))
        maxRob[0] = nums[0]
        maxRob[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            maxRob[i] = max(nums[i] + maxRob[i - 2], maxRob[i-1])
            print(i, maxRob[i])

        return maxRob[len(nums) - 1]
        