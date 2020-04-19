class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return 0
        start, end = 0, len(nums) - 1
        if nums[start] <= nums[end]:
            return nums[start]
        while start < end - 1:
            mid = start + (end - start) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] >= nums[start]:
                start = mid
            if nums[mid] <= nums[end]:
                end = mid

        return nums[start + 1]

"""
153. Find Minimum in Rotated Sorted Array
Medium

1753

216

Add to List

Share
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""