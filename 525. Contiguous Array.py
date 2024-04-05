class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map_ = {}
        count = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            if count in map_:
                res = max(res, i - map_[count])
            elif count == 0:
                res = i + 1
            else:
                map_[count] = i

        return res
