class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []

        seen = set()

        last_occurance = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:

                while stack and c < stack[-1] and i < last_occurance[stack[-1]]:
                    seen.remove(stack.pop())

                seen.add(c)
                stack.append(c)

        return ''.join(stack)
        # set ={c, b, a}
        # [c, b, a] -< c
        # cbacdcbc
        # c b a c
        # b a c d c
