class Solution:
    # correct
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    # not pass
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        import re
        #s = re.sub(" ", "0", s)
        s = re.sub(r'\W+', '', s)
        s = s.lower()
        #s = ''.join(filter(str.isalpha, s.lower()))

        if len(s) <= 1:
            return True
        out = ""
        for i in range(len(s)):
            if i < len(s) and i > 0 and s[i] == s[i - 1]:
                return True
            if s[i] == "0" and i > 0 and i < len(s) and s[i + 1] == s[i - 1]:
                return True
            # odd len
            curr = self.helper(s, i, i)
            if len(curr) > len(out):
                out = curr
            # even len
            curr = self.helper(s, i, i + 1)
            if len(curr) > len(out):
                out = curr  
        return len(out) >= 2
        
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right] and s[left] != "0":
            left -= 1
            right += 1
        return s[left + 1: right]
