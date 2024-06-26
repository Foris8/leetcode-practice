class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = {0: 0}

        for r in wall:
            total = 0

            for b in r[:-1]:
                total += b
                if total not in countGap:
                    countGap[total] = 1
                else:
                    countGap[total] += 1

        return len(wall) - max(countGap.values())
#sadasd