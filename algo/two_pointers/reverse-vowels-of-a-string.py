class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)

        idx_vow = []
        for idx, char in enumerate(l):
            if char.lower()  in ['a','e','i','o','u']:
                idx_vow.append(idx)

        left, right = 0, len(idx_vow) - 1
        while left < right:
            l[idx_vow[left]],l[idx_vow[right]] = l[idx_vow[right]],l[idx_vow[left]]
            left += 1
            right -= 1
        return "".join(l)

            
"""
345. Reverse Vowels of a String
Easy

478

870

Favorite

Share
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""
