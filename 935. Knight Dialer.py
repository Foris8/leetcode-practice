class Solution:
    def knightDialer(self, n: int) -> int:
        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        mod = 10 ** 9 + 7

        # dp[remain][n] -> remain nth number - ? #number of combinations

        dp = [[0] * 10 for _ in range(n)]
        for i in range(10):
            dp[0][i] = 1

        for remain in range(1, n):
            for number in range(10):
                ans = 0

                for next_s in jumps[number]:
                    ans = (ans + dp[remain-1][next_s]) % mod

                dp[remain][number] = ans

        ans = 0
        for square in range(10):
            ans = (ans + dp[n - 1][square]) % mod

        return ans
