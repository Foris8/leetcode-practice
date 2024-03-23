class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[j] -> under amount j, the minimun number

        # dp[j] = min(dp[j], dp[j-coins[i]] + 1)

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for j in range(1, amount+1):
            for i in range(len(coins)):
                if j-coins[i] >= 0 and dp[j-coins[i]] != float('inf'):
                    dp[j] = min(dp[j], dp[j-coins[i]]+1)

        if dp[amount] == float("inf"):
            return -1

        return dp[amount]
