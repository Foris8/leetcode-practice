class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash_map = dict()
        count = 0

        for i in nums1:
            for j in nums2:
                two_sum = i + j
                if two_sum in hash_map:
                    hash_map[two_sum] += 1
                else:
                    hash_map[two_sum] = 1

        for i in nums3:
            for j in nums4:
                key = -i - j
                if key in hash_map:
                    count += hash_map[key]

        return count
