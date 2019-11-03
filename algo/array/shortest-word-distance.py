class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1 = [i for i in range(len(words)) if words[i] == word1]
        w2 = [i for i in range(len(words)) if words[i] == word2]
        
        return min([abs(i - j) for i in w1 for j in w2])
        
"""
243. Shortest Word Distance
Easy

323

31

Favorite

Share
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""

class WordDistance_II(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        from collections import defaultdict
        self.loc = defaultdict(list)
        for idx, word in enumerate(words):
            self.loc[word].append(idx)
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        loc1 = self.loc[word1]
        loc2 = self.loc[word2]
        l1, l2 = 0, 0
        min_diff = float("inf")
        
        while l1 < len(loc1) and l2 < len(loc2):
            min_diff = min(min_diff, abs(loc1[l1] - loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1
        return min_diff

        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

"""
244. Shortest Word Distance II
Medium

255

95

Favorite

Share
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""

class Solution(object):
    def shortestWordDistance_III(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1 = [i for i in range(len(words)) if words[i] == word1]
        w2 = [i for i in range(len(words)) if words[i] == word2]
        
        
        return min([abs(i - j) for i in w1 for j in w2 if i != j])
        
"""
245. Shortest Word Distance III
Medium

146

63

Favorite

Share
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:
You may assume word1 and word2 are both in the list.
"""
