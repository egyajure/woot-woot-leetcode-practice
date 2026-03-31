class Solution:
    def climbStairs(self, n: int) -> int:
        # base case
        if (n < 3):
            return n

        # let steps[i] be the number of ways to reach step i
        steps = [0] * (n+1)

        # base cases
        steps[1] = 1
        steps[2] = 2

        for i in range (3, n + 1):
            steps[i] = steps[i - 1] + steps[i -2]
        
        return steps[n]
        