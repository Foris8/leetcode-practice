class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            ele = s[i]
            if ele == "(":
                stack.append((ele, i))
            elif ele == ")":

                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((ele, i))

        for t in stack:
            a, index = t
            s = s[:index] + " " + s[index + 1:]

        return s.replace(" ", "")
