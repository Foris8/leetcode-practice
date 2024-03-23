class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0] * (n+1)

        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            print(i)
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n]
