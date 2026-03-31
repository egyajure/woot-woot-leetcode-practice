class Solution:
    # greedy algo
    # for each jump you jump to the available position with the furthest reach
    # max value of idx + value
        

    def canJump(self, nums: List[int]) -> bool:
        def Jump(idx, nums:List[int]) -> bool:
            print(idx)

            if (idx + nums[idx] >= len(nums) -1):
                return True
            if (nums[idx] <= 0):
                return False
            
            best_idx = idx + 1
            best_val = 0

            print("find next")
            for rangeNum in range(1, nums[idx] + 1):
                print(rangeNum)
                if (idx + rangeNum + nums[idx + rangeNum] > best_val):
                    best_val = idx + rangeNum + nums[idx + rangeNum]
                    best_idx = idx + rangeNum
            
            return Jump(best_idx, nums)

        return Jump(0, nums)

