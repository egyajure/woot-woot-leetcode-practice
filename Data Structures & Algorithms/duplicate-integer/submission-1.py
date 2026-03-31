class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:


        # solution that came to mind first - sort the array and use two pointers to see if there are two of the same
        # solution that better utilizes data structures - use a set!

        foundNums = set()
        
        for num in nums:
            if num in foundNums:
                return True
            foundNums.add(num)

        return False