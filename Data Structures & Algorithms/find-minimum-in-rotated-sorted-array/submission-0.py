class Solution:
    def findMin(self, nums: List[int]) -> int:

        # for a given subset of this list, if the left value is smaller than the right value, there has been no flip
        # ex 781234 -> l > r, the minimum is in this list
        # 234 -> l < r, the minimum is not in this list
        # 781 -> l > r, the minimum is in this lists
        # 81 -> the minimum is in this list
        # 1 we found it

        l, r = 0, len(nums) - 1

        while r - l > 1:
            m = l + (r-l)//2

            if (nums[m] < nums[r]):
                r = m
            else:
                l = m
        
        return min(nums[l], nums[r])
        