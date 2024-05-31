class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_ = {}

        for i, num in enumerate(nums):
            if num in dict_ and i - dict_[num] <= k:
                return True

            dict_[num] = i

        return False
