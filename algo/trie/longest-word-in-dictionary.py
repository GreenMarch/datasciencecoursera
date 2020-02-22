# class TrieNode:
#     def __init__(self, ):
#         self.children = collections.defaultdict(TrieNode)
#         self.isword = False
#
#
# class Solution:
#     def longestWord(self, words: List[str]) -> str:
#         words.sort(key=lambda x: [-len(x), x], reverse=True)
#         ans = ""
#         self.root = TrieNode()
#         for word in words:
#             if len(word) > len(ans) + 1:
#                 return ans
#             if self.insert(word):
#                 ans = word
#         return ans
#
#     def insert(self, word):
#         cur = self.root
#         for i in range(len(word) - 1):
#             cur = cur.children[word[i]]
#             if not cur.isword:
#                 return False
#         cur = cur.children[word[-1]]
#         cur.isword = True
#         return True

class Solution:
    def longestWord(self, words):
        words.sort()
        lw = ""
        wordset = set(["",])
        for w in words:
            if w[:-1] in wordset:
                if len(w) > len(lw):
                    lw = w
                wordset.add(w)
        return lw

"""
720. Longest Word in Dictionary
Easy

490

602

Add to List

Share
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].

in = ["w","wo","wor","worl","world"]
out = "world"
"""