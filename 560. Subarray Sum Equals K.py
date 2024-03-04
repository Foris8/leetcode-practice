class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # 1 1 1
        # prefix = 1
        # prefix[1] = 2
        # prefix[2] = 3
        # say iii and jjj is at a difference of kkk i.e. if sum[i]−sum[j]=ksum[i] - sum[j] = ksum[i]−sum[j]=k,
        # the sum of elements lying between indices i and j is k.
        dict_ = {
            nums[0]: 1
        }

        prefix_sum = nums[0]
        res = 0

        for num in nums:
            prefix_sum += num

            prev_sum = prefix_sum - k
            if prev_sum in dict_:
                res += dict_[prev_sum]

            if prefix_sum in dict_:
                dict_[prefix_sum] += 1
            else:
                dict_[prefix_sum] = 1

        return res
