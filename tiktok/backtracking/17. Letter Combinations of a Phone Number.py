class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dict_ = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        self.dfs(digits, 0, "", res, dict_)

        return res

    def dfs(self, digits, startIndex, record, res, dict_):
        # stop condition
        if len(record) == len(digits):
            res.append(record)
            return

        letter = digits[startIndex]

        letters = dict_[letter]

        # trasverse
        for i in letters:
            record += i
            self.dfs(digits, startIndex + 1, record, res, dict_)
            record = record[:-1]
