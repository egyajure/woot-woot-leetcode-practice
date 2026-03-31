class Solution:
    def __init__(self):
        self.minCoins = {}

    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(curAmount):
            if curAmount == 0:
                return 0
            if curAmount < 0:
                return -1
            if curAmount in self.minCoins:
                return self.minCoins[curAmount]
            
            minNum = float('inf')
            for coin in coins:
                res = dfs(curAmount - coin)
                if res != -1:
                    minNum = min(minNum, res + 1)  # add 1 coin to result
            
            self.minCoins[curAmount] = -1 if minNum == float('inf') else minNum
            return self.minCoins[curAmount]
        
        return dfs(amount)

        