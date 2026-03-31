class Solution:
    def isValid(self, s: str) -> bool:
        # you could do this with a stack but since the ONLY characters are (){}[]
        # we can do this with a 2 pointer

        matching = {'(': ')', '[':']', '{':'}'}

        if (len(s) % 2 != 0):
            return False

        stack = []

        for char in s:
            if (char in matching):
                stack.append(char)
            else:
                if (len(stack) == 0):
                    return False
                temp = stack.pop()
                if (char != matching[temp]):
                    return False
        
        return len(stack) == 0
    