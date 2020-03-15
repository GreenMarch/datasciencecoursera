class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :param words: List[str]
        :param pattern: str
        :return: List[str]
        """
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                print("w, p =", w, p)
                print("index =",word.index(w))
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    print("not matched,",(m1[w], m2[p]),(p, w))
                    return False
                else:
                    print("matched,",(m1[w], m2[p]),(p, w))
            return True

        return filter(match, words)


input_words = ["abc","deq","mee","aqq","dkd","ccc"]
input_pattern = "abb"

print(list(Solution().findAndReplacePattern(input_words, input_pattern)))