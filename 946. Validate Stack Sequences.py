class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        l = 0
        r = 0
        n = len(pushed)

        while l < n:
            while stack and stack[-1] == popped[r]:
                stack.pop()
                r += 1

            stack.append(pushed[l])
            l += 1

        while stack:
            if stack[-1] == popped[r]:
                stack.pop()
                r += 1
            else:
                return False
        return True
