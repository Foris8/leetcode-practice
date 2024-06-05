class Solution:
    def minimumKeypresses(self, s: str) -> int:
        record = Counter(s)
        res = []

        for k, v in record.items():
            res.append(v)

        res.sort(reverse=True)

        steps = 0
        n = 9
        cost = 1

        for c in res:
            if n > 0:
                steps += c * cost
                n -= 1
            else:
                n = 9
                cost += 1
                steps += c * cost
                n -= 1
        return steps
