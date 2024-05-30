class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        hashmap[0] = -1

        sum_ = 0

        for i, num in enumerate(nums):
            sum_ += num

            if sum_ % k in hashmap:
                if i - hashmap[sum_ % k] >= 2:
                    return True
                else:
                    continue

            hashmap[sum_ % k] = i

        return False
