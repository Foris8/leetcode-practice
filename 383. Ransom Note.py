class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = dict()

        for i in magazine:
            if i not in record:
                record[i] = 1
            else:
                record[i] += 1

        for i in ransomNote:
            if i not in record:
                return False

            record[i] -= 1
            if record[i] < 0:
                return False

        return True
