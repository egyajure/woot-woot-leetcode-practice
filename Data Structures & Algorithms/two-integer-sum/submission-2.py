class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have two pointers and then add them to see if they equal the target
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []