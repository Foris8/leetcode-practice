class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        # identify the dp set
        dp = [0] * (n+1)

        # recursion formual dp[n] = dp[n-1] + dp[n-2]

        # Initiaze the dp
        dp[0] = 0
        dp[1] = 1

        # dp[2] = dp[0] + dp[1]
        # 1 = 1 + 0

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
