class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for word in s:
            if not stack or stack[-1] != word:
                stack.append(word)
            elif stack[-1] == word:
                stack.pop()

        return ''.join(stack)
