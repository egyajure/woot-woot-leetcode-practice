class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = defaultdict(list)

        for i, num in enumerate(nums):
            indexes[num].append(i)
        
        for i in range(len(nums)):
            sub_target = target - nums[i]
            if sub_target in indexes:
                if (sub_target != nums[i]):
                    return[i, indexes[sub_target][0]]
                else:
                    if (len(indexes[sub_target]) > 1):
                        return[i, indexes[sub_target][1]]
        
        return [-1, -1]
                

