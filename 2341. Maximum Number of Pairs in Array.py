class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dict_ = {}

        for num in nums:
            if num not in dict_:
                dict_[num] = 1
            else:
                dict_[num] += 1
        pairs = 0
        leftover = 0

        for k, v in dict_.items():
            pairs += v // 2
            leftover += v % 2

        return [pairs, leftover]
