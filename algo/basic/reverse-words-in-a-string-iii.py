class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        return " ".join([w[::-1] for w in word])
