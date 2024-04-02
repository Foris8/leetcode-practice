class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        res = collections.defaultdict(list)

        for word in words:
            odd, even = "", ""

            for i, char in enumerate(word):
                if i % 2 == 0:
                    even += char
                else:
                    odd += char

            odd = sorted(odd)
            even = sorted(even)

            final = "".join(odd+even)
            res[final].append(word)

        return len(res)
