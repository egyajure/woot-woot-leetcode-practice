class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # exactly one answer
        # because there is one answer you can kind of rule them out
        # ex: 3,4,5,6 target = 7
        # we start with 3 + 6 = 9, too big
        # we can only make our other number bigger, thus 6 is not an option, move the right pointer to the left
        # if our target was 11, 3 could not be an option because moving the other number only makes the answer smaller, move the left pointer to the right

        # there is a faster way! It is actually faster to store all the elements in a hash map then to store all of the elements
        # also another hint here - sorting while maintaining original order is difficult! avoid when possible

        # start by keeping track of where the occurences of the indexes are
        # we are basically looking for the index of the second value

        indexes = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in indexes:
                return [indexes[needed], i]
            
            indexes[num] = i
        
        return [-1, -1]