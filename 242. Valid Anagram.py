#Hash set
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_set = [0] * 26

        for i in s:
            index = int(ord(i)-ord('a'))
            hash_set[index] += 1

        for j in t:
            index = int(ord(j)-ord('a'))
            hash_set[index] -= 1

        for i in hash_set:
            if i != 0:
                return False

        return True

#hash set
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for x in s:
            s_dict[x] += 1

        for x in t:
            t_dict[x] += 1
        return s_dict == t_dict
