class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for ele in num:

            while k and stack and int(stack[-1]) > int(ele):
                stack.pop()
                k -= 1
            stack.append(ele)

        if k:
            stack = stack[:-k]

        res = "".join(stack)
        return res.lstrip("0") or "0"
