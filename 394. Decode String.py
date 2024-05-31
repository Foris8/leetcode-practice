class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""

        for c in s:
            if c == "]":
                curr = ""
                while stack[-1] != "[":
                    curr = stack.pop() + curr
                # pop [
                stack.pop()

                # pop element
                muli = ""
                while stack and stack[-1].isdigit():
                    muli = stack.pop() + muli

                stack.append(int(muli) * curr)
            else:
                stack.append(c)
        return "".join(stack)
