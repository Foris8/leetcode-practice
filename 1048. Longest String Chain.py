class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # dp[i] -> ith index as end, max number of word chain
        # dp[i] = max(dp[i],dp[j]+1)
        words.sort(key=len)
        dp = {}
        max_chain = 0
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                if prev_word in dp:
                    dp[word] = max(dp[word], dp[prev_word] + 1)
            max_chain = max(max_chain, dp[word])
        return max_chain
