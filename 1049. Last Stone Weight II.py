class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # why dp
        # since the curr state from prev state

        # [2,7,4,1,8,1] -> [2, 7 , 1, 8 , 1]

        total_sum = sum(stones)

        target = total_sum // 2

        # dp[i][j] -> [0,i-1th] tiems, max weigth at j capacity

        dp = [[0 for j in range(target + 1)] for i in range(len(stones))]

        for i in range(stones[0], target + 1):
            dp[0][i] = stones[0]

        for i in range(len(stones)):
            for j in range(target + 1):
                if j < stones[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1]
                                   [j-stones[i]] + stones[i])

        print(dp)
        return (total_sum - 2 * dp[len(stones)-1][target]) 