class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # words = set(wordDict)
        # queue = deque([0])
        # seen = set()

        # while queue:
        #     start = queue.popleft()
        #     if start == len(s):
        #         return True

        #     for end in range(start + 1, len(s) + 1):
        #         if end in seen:
        #             continue

        #         if s[start:end] in words:
        #             queue.append(end)
        #             seen.add(end)

        # return False

        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)

        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordSet:
                    dp[i] = True

        return dp[-1]
