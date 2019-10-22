class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        # build hash map : character and how often it appears
        count = Counter(s)
        print(count)
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
'''
387. First Unique Character in a String
Easy

1239

87

Favorite

Share
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''
