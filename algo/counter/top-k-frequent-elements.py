from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = Counter(nums).most_common(k)
        out = [None]*k
        for i in range(k):
            out[i] = result[i][0]
        return out

from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        top_k = list(zip(*count.most_common(k)))[0]
        return top_k
        
"""
347. Top K Frequent Elements
Medium

1958

126

Favorite

Share
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
