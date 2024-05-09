class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        queue = deque(happiness)
        iteration = 0
        res = 0

        while iteration < k:
            curr = queue.popleft() - iteration

            if curr <= 0:
                break
            else:
                res += curr

            iteration += 1

        return res
