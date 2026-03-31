class Solution:
    def __init__(self):
        self.minCoins = {}

    # first, top-down
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     # what choice are we making? which coin to use for a given amount
    #     # we only have one minimum number of coins per total, so we can store that in a dict once we find it

    #     if (amount == 0):
    #         return 0
    #     if (amount < 0):
    #         return -1
    #     if (amount in self.minCoins):
    #         return self.minCoins[amount]

    #     minAmount = float('inf')
    #     for coin in coins:
    #         temp = self.coinChange(coins, amount-coin) # spending one coin, reducing the total by that coin
    #         if (temp != -1):
    #             minAmount = min(minAmount, temp + 1)
        
    #     self.minCoins[amount] = minAmount
    #     return minAmount if minAmount != float('inf') else -1
    
    # next, bottom up
    # this is a little trickier because our old base cases don't feel as applicable
    # the amount to get n amount is the minimum of the amount to get n - coin amount

    def coinChange(self, coins: List[int], amount: int) -> int:

        coinsNeeded = [-1] * (amount + 1)
        coinsNeeded [0] = 0

        for coin in coins:
            if (coin <= amount):
                coinsNeeded[coin] = 1

        for i in range(1, amount + 1):
            minVal = float('inf')
            for coin in coins:
                if (i - coin >= 0):
                    temp = coinsNeeded[i - coin] + 1
                    if (temp != 0):
                        minVal = min(minVal, temp)
            coinsNeeded[i] = minVal if minVal != float('inf') else -1

        print(coinsNeeded)
        return coinsNeeded[amount]
