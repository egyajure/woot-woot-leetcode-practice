class Solution:
    def rob(self, nums: List[int]) -> int:
        # let maxRob[i] be the max amount of money you can rob from houses 1-i
        # thus our answer is located in maxRob[len(nums) - 1]

        #mmaxRob[x] = nums[x] + maxRob[x-2] (because you can't rob the next house)
        # or maxRob[x-1]

        if (len(nums) == 1):
            return nums[0]

        maxRob = [0] * len(nums)

        # base cases
        maxRob[0] = nums[0]
        maxRob[1] = max(maxRob[0], nums[1])

        for i in range (2, len(nums)):
            maxRob[i] = max(maxRob[i-1], nums[i] + maxRob[i-2])
        
        return maxRob[len(nums) - 1]