class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp[i][j] -> the minimum sum at this cell

        dp = [[0] * len(grid[0]) for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if i-1 >= 0 and j-1 < 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif j-1 >= 0 and i-1 < 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j] + grid[i][j],
                                   dp[i][j-1] + grid[i][j])

        return dp[-1][-1]
