class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.lower().split()[-1])
        
'''58. Length of Last Word
Easy

459

1882

Favorite

Share
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''
