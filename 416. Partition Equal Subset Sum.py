class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2

        # dp[i][j] -> max value choseon from [0,i-1] index with limit of j as max value

        # dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]]+nums[i])

        # initialize dp[][]
        dp = [[0 for j in range(target + 1)] for i in range(len(nums))]

        for i in range(nums[0], target+1):
            dp[0][i] = nums[0]

        for i in range(1, len(nums)):
            for j in range(target+1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:

                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]] + nums[i])

        return dp[len(nums)-1][target] == target
