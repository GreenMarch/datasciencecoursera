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

    """
    # slow
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            j = i + 1
            while j <= len(s) and len(res) <= len(s[i:]):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) >= len(res):
                    res = s[i:j]
                j += 1
        return res
        
    """
    
    """
    5. Longest Palindromic Substring
Medium

4724

423

Favorite

Share
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
