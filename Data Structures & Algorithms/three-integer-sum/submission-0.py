class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3Sum is basically 2Sum done n times, with a fixed third value
        # Since we don't want duplicates,
        # we can force 1 < 2 < 3 by shifting the size of the 2Sum
        # ex if n1 = -5, n2 + n3 = 5


        if (len(nums) < 3):
            return []

        ans = set()

        nums.sort()

        for i, num in enumerate(nums):
            # i is the base value here
            l, r = i + 1, len(nums) - 1

            goal = 0 - num

            # 2Sum
            while (l < r):
                if (nums[l] + nums[r] == goal):
                    ans.add((nums[i], nums[l], nums[r]))
                    l +=1
                    r -=1
                elif(nums[l] + nums[r] > goal):
                    r -= 1
                else:
                    l += 1
        
        return list(ans)