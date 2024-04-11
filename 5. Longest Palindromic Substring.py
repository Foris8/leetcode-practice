class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            left = i
            right = j

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        ans = [0, 0]

        for i in range(len(s)):
            odd_len = expand(i, i)
            if odd_len > ans[1] - ans[0] + 1:
                dist = odd_len // 2
                ans = [i-dist, i+dist]

            even_length = expand(i, i+1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]

        i, j = ans

        return s[i: j+1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s))]

        res = [0, 0]

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j-i <= 1:
                        dp[i][j] = True

                        if j-i >= res[1] - res[0]:
                            res[0], res[1] = i, j
                    elif dp[i+1][j-1]:

                        dp[i][j] = True

                        if j-i >= res[1] - res[0]:
                            res[0], res[1] = i, j

        i, j = res
        return s[i:j+1]
