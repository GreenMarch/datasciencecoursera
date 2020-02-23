import heapq

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        heap = []
        for n in nums:
            heapq.heappush(heap, a*(n**2) + b*(n) + c)
        heapq.heapify(heap)
        return heapq.nsmallest(len(heap), heap)

"""
360. Sort Transformed Array
Medium

281

86

Add to List

Share
Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
"""