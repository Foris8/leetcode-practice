class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # def the max profit
        # dp[i] -> max value under his day

        length = len(prices)
        if length == 0:
            return 0

        dp = [[0]*2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i]+dp[i-1][0])

        return dp[-1][1]
