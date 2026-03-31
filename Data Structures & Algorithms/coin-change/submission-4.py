class Solution:
    def __init__(self):
        self.minCoins = {}

    # first, top-down
    def coinChange(self, coins: List[int], amount: int) -> int:
        # what choice are we making? which coin to use for a given amount
        # we only have one minimum number of coins per total, so we can store that in a dict once we find it

        if (amount == 0):
            return 0
        if (amount < 0):
            return -1
        if (amount in self.minCoins):
            return self.minCoins[amount]

        minAmount = float('inf')
        for coin in coins:
            temp = self.coinChange(coins, amount-coin) # spending one coin, reducing the total by that coin
            if (temp != -1):
                minAmount = min(minAmount, temp + 1)
        
        self.minCoins[amount] = minAmount
        return minAmount if minAmount != float('inf') else -1
        