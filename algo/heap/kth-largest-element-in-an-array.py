import heapq
class Solution:
    def findKthLargest(self, nums, k):
        # nums.sort()
        # return nums[len(nums) - k]
        heap = nums
        heapq.heapify(heap)
        for i in range(len(nums) - k + 1):
            print("i", i)
            res = heapq.heappop(heap)
        return res

data = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(data, k))

"""
215. Kth Largest Element in an Array
Medium

2941

208

Add to List

Share
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
"""