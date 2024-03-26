class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # only have two states ,
        # dp[i][1] ->have stock max(dp[i-1][1],dp[i-1][0] - prices[i])
        # dp[i][0] -> don' have stock max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)

        length = len(prices)

        dp = [[0]*2 for _ in range(length)]

        dp[0][1] = -prices[0]

        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[-1][0]
