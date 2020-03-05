class Solution:
    def reverseWords(self, s):
        """

        :param s: str
        :return: str
        """
        word = s.split()
        return " ".join([w[::-1] for w in word])

data = "abc"
print(Solution().reverseWords(data))