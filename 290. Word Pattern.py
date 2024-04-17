class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict_ = {}
        dict_word = {}

        s = s.split(" ")

        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            p = pattern[i]
            word = s[i]

            if p not in dict_:
                if word not in dict_word:
                    dict_word[word] = p
                    dict_[p] = word
                else:
                    return False
            else:
                if dict_[p] != word:
                    return False

        return True
