class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = {}
        for item in s:
            dic[item] = dic.get(item, 0) + 1
        count1 = 0
        for val in dic.values():
            if val % 2 == 1:
                count1 += 1
            if count1 > 1:
                return False
        return True
"""
266. Palindrome Permutation
Easy

244

42

Favorite

Share
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""
