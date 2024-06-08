class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dict_ = collections.defaultdict(int)

        for c in s:
            dict_[c] += 1

        res = ""

        for c in order:
            res += dict_[c] * c
            del dict_[c]

        for k, v in dict_.items():
            res += v * k
        return res
