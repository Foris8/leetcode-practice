class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        right = 0

        dict_ = collections.defaultdict(int)

        res = 0

        while right < len(s):

            dict_[s[right]] += 1

            while len(dict_) > 2:

                dict_[s[left]] -= 1
                if dict_[s[left]] == 0:
                    del dict_[s[left]]

                left += 1

            right += 1
            res = max(res, right - left)

        return res
