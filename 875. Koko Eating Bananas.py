class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [4, 11, 20, 23, 30]
        # k = ? h =?

        # if h= len(piles) : max
        # if h < len(piles): imposible
        # if h > len(piles)

        left = 1
        right = max(piles)
        res = right
        while left <= right:
            k = (left + right) // 2

            total_sum = 0

            for i in piles:
                total_sum += math.ceil(i/k)

            if total_sum <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        return res
