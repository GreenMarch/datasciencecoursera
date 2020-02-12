class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(x for x in s.split()[::-1])
        # return " ".join(reversed(s.split())
        # return " ".join((s.split()[::-1])
