class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1
        def isPalin(s):
            return s==s[::-1] 
        while l<r:
            if s[l]!=s[r]:
                return isPalin(s[l+1:r+1]) or isPalin(s[l:r])
            l += 1
            r -= 1
        return True
        """
        for i in xrange(len(s)):
            t = s[:i] + s[i + 1:]
            if t == t[::-1]: return True

        return s == s[::-1]
        """
        
"""
680. Valid Palindrome II
Easy

990

69

Favorite

Share
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""
