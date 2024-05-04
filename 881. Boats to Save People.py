class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1

        res = 0

        while left <= right:
            cur_sum = people[left] + people[right]
            res += 1
            if cur_sum <= limit:
                left += 1
                right -= 1
            else:
                right -= 1

        return res
