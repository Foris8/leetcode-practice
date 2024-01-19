class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()

        left = 0
        right = len(s) - 1

        while right > left:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1
        return " ".join(s)
