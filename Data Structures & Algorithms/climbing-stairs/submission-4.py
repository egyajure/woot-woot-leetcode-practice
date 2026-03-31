class Solution:
    numSteps = {}

    def __init__(self):
        self.numSteps = {}

    # first, top down (recursive)
    # def climbStairs(self, n: int) -> int:
    #     if (n == 1):
    #         return 1
    #     if (n == 2):
    #         return 2
    #     if (n in self.numSteps):
    #         return self.numSteps[n]

    #     steps = self.climbStairs(n-1) + self.climbStairs(n-2)
    #     self.numSteps[n] = steps
    #     return steps

    # next, bottom up (iterative)
    # def climbStairs(self, n: int) -> int:
    #     if (n == 1):
    #         return 1
    #     if (n == 2):
    #         return 2
        
    #     steps = [0] * (n + 1)
    #     steps[1] = 1
    #     steps[2] = 2

    #     for i in range (3, n + 1):
    #         steps[i] = steps[i-1] + steps[i-2]

    #     return steps[n]

    
    # lastly, notice how we only care about the previous two values, we can optimize further
    def climbStairs(self, n: int) -> int:
        if (n == 1):
            return 1
        if (n == 2):
            return 2
        
        two_behind = 1
        one_behind = 2

        # we're starting at 3

        for i in range (3, n + 1):
            cur = one_behind + two_behind
            two_behind = one_behind
            one_behind = cur

        return cur


        