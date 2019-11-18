class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        def f(s):
            if s not in d:
                maxL = 0    
                for c in set(s):
                    i, j = s.find(c), s.rfind(c)
                    maxL = max(maxL, 1 if i==j else 2+f(s[i+1:j]))
                d[s] = maxL
            return d[s]
        return f(s)
    
        """
        out = 0
        for i in range(1, len(s) - 1):
            l, r = i - 1, i + 1
            while l >= 0 and r <= len(s):
                new_s = s[l:i] + s[i + 1:r]
                if self.is_pal(new_s) == True:
                    print("l, r: " + str(l) + str(r))
                    out = max(len(new_s), out)
                l -= 1
                r += 1
        return out
            
    def is_pal(self, string1):
        if string1 and string1 == string1[::-1]:
            return True
        else:
            return False
    """ 
        
"""
516. Longest Palindromic Subsequence
Medium

1206

152

Favorite

Share
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""
