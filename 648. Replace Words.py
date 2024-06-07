class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        record = set(dictionary)

        sentence = sentence.split(" ")

        res = []

        for i, word in enumerate(sentence):
            for j in range(len(word)):
                if word[:j+1] in record:
                    sentence[i] = word[:j+1]
                    break
        return " ".join(sentence)
