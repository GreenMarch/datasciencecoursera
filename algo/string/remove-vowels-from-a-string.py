class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        l = list(S)
        out = []
        print("l: " + str(l))
        for i in range(len(l)):
            if l[i] not in ['a', 'e', 'i', 'o', 'u']:
                out.append(l[i])
        return "".join(out)
        
        
"""
1119. Remove Vowels from a String
Easy

33

54

Favorite

Share
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: "aeiou"
Output: ""
 

Note:

S consists of lowercase English letters only.
1 <= S.length <= 1000
"""
