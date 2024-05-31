class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        map_ = Counter(nums)
        res = []

        for k, v in map_.items():
            if v == 1:
                res.append(k)
        return res
