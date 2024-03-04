class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = 0
        b = 0

        left = 0
        right = 0

        while right < len(colors):
            # if it is A
            if colors[right] == "A" and right < len(colors):
                while right < len(colors) and colors[right] == "A":
                    right += 1

                count = right - left
                if count >= 3:
                    a += count - 2
                left = right
            else:
                while right < len(colors) and colors[right] == "B":
                    right += 1

                count = right - left
                if count >= 3:
                    b += count - 2
                left = right

        if a <= b:
            return False
        else:
            return True
