class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        hamsters = list(hamsters)

        for i, c in enumerate(hamsters):
            if c == "H":

                if i - 1 >= 0 and hamsters[i-1] == "#":
                    continue

                if (i + 1 < len(hamsters) and hamsters[i+1] == "."):
                    hamsters[i+1] = "#"
                elif (i-1 >= 0 and hamsters[i-1] == "."):
                    hamsters[i-1] = "#"
                else:
                    return -1

        res = Counter(hamsters)

        return res['#']
