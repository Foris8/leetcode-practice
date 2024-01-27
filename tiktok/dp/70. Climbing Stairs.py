class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        # Identify the meaning of the dp
        # The dp set is defined as the number of step of i
        dp = [0] * n

        # Recursion formular:
        # dp[i] = dp[i-1] + dp[i-2] + 1

        # initiazizaing
        dp[0] = 1  # step one
        dp[1] = 2  # step one

        # transverse
        for i in range(2, n):
            dp[i] = max(dp[i-1] + dp[i-2], dp[i])

        # n = 1 -> 1
        # n = 2 - > 2
        # n = 3 -> 1 + 2
        return dp[-1]
