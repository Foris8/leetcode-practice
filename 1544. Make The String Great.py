class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for ele in s:
            if stack and abs(ord(stack[-1]) - ord(ele)) == 32:
                stack.pop()
            else:
                stack.append(ele)

        return "".join(stack)
