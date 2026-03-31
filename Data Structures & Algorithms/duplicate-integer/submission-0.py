class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = []
        for a in nums:
            if a in vals:
                return True
            vals.append(a)
        return False
        
         