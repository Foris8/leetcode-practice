class Solution:
    def calculate(self, s: str) -> int:
        # "3+222*2/3"
        # [3,+, 222, *, 2]
        num, PreSign, stack = 0, '+', []
        for c in s+'+':
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if PreSign == '+':
                    stack.append(num)
                elif PreSign == '-':
                    stack.append(-num)
                elif PreSign == '*':
                    stack.append(stack.pop()*num)
                elif PreSign == '/':
                    stack.append(math.trunc(stack.pop()/num))
                PreSign = c
                num = 0
        return sum(stack)
