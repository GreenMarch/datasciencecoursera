class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        from collections import Counter
        ch_ctr = Counter(chars)
        
        good = 0
        for word in words:
            w_ctr = Counter(word)
            isGood = True
            for key in w_ctr:
                if key not in ch_ctr or w_ctr[key] > ch_ctr[key]:
                    isGood = False
                    break
            if isGood == True:
                    good += len(word)
        return good
"""
1160. Find Words That Can Be Formed by Characters
Easy

122

31

Favorite

Share
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
"""
