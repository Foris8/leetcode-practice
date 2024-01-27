class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(len(dp)):
            dp[i][0] = 1

        for j in range(len(dp[0])):
            dp[0][j] = 1

        for i in range(1, len(dp)):  # i is the row
            for j in range(1, len(dp[0])):  # j is the col
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
