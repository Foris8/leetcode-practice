class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][1] - >ith  not prossess stock max money
        # dp[i][0] -> ith day prossess stock max money

        # dp[i][0] = max(dp[i-1][0], -prices[i] + dp[i-1][1])
        # do[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])

        length = len(prices)
        dp = [[0] * 2 for _ in range(length)]

        dp[0][0] = -prices[0]

        dp[0][1] = 0

        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], -prices[i] + dp[i-1][1])
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])

        return dp[-1][-1]
