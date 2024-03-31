class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        res = -1

        a_point = 0
        b_point = 0

        n = len(possible)
        a_sum = 0
        b_sum = sum(possible)

        for i in range(n-1):
            a_sum += possible[i]
            b_sum -= possible[i]
            a_point = a_sum + (n-(i+1) - b_sum)
            b_point = b_sum + (i+1 - a_sum)

            if a_point > b_point:
                return i+1

        return -1
