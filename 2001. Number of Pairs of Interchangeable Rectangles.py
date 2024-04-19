class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        dict_ = collections.defaultdict(int)
        res = 0
        for rec in rectangles:
            w, h = rec
            ratio = w / h

            dict_[ratio] += 1

        for c in dict_.values():
            res += (c * (c - 1)) // 2

        return res
