import heapq
class Solution:
    def kthSmallest(self, matrix, k):
        nums = []
        for row in matrix:
            for val in row:
                nums.append(val)
        heapq.heapify(nums)
        return heapq.nsmallest(k, nums)[-1]

data = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

print(Solution().kthSmallest(data, k))

"""
378. Kth Smallest Element in a Sorted Matrix
Medium

1780

106

Add to List

Share
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""