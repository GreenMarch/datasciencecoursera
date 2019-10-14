class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ""
        for i in range(len(s)):
            # odd len
            curr = self.helper(s, i, i)
            if len(curr) > len(out):
                out = curr
            # even len
            curr = self.helper(s, i, i + 1)
            if len(curr) > len(out):
                out = curr            
        return out
        
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]
