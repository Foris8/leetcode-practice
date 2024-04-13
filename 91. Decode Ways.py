class Solution:
    def numDecodings(self, s: str) -> int:
        # 226
        # 2
        # 22
        # 2

        # 2 26
        # 22 6
        # 2 2 6
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        if not s or s[0] == '0':
            return 0

        for i in range(2, n+1):
            one = int(s[i-1])
            two = int(s[i-2:i])

            if one != 0:
                dp[i] += dp[i-1]

            if 10 <= two <= 26:
                dp[i] += dp[i-2]
        return dp[n]
