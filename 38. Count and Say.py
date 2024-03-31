class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        next_say = self.countAndSay(n-1)
        res = ""
        count = 1
        digit = next_say[0]

        for i in range(1, len(next_say)):
            if next_say[i] == digit:
                count += 1
            else:
                res += str(count) + digit
                count = 1
                digit = next_say[i]

        res += str(count) + digit
        
        return res
