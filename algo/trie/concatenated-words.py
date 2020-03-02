class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        res = []
        t = Trie()
        for word in words:
            t.add(word)
        for word in words:
            if t.helper(word, 0, len(word) - 1, 0):
                res.append(word)
        return res


class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = Node()
            p = p.children[c]
        p.is_end = True


    def helper(self, word, st, end, cnt):
        p = self.root
        for x in range(st, end + 1):
            if word[x] in p.children:
                p = p.children[word[x]]
                if p.is_end:
                    if x == end:
                        return cnt >= 1
                    if self.helper(word, x + 1, end, cnt + 1):
                        return True
            else:
                break
        return False

"""
472. Concatenated Words
Hard

473

85

Add to List

Share
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
"""