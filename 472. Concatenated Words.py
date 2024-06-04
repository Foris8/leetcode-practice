class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dictionary = set(words)
        answer = []

        for word in words:
            length = len(word)
            dp = [False] * (length + 1)
            dp[0] = True

            for i in range(1, length + 1):
                for j in range(1 if i == length else 0, i):
                    if dp[i]:
                        break
                    dp[i] = dp[j] and word[j:i] in dictionary

            if dp[length]:
                answer.append(word)

        return answer
