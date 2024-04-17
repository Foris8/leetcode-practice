class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict_ = collections.defaultdict(int)

        for char in text:
            dict_[char] += 1

        res = 0

        check = True

        while check:

            for char in "balloon":

                if dict_[char] >= 1:
                    dict_[char] -= 1
                else:
                    check = False
                    break

            res += 1

        return res - 1
