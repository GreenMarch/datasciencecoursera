class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """ 
        l, r = 0, len(nums) - 1
        while l <= r:
            pivot = l + (r - l) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] >= nums[l]:
                if target >= nums[l] and target < nums[pivot]:
                    r = pivot - 1
                else:
                    l = pivot + 1
            else:
                if target <= nums[r] and target > nums[pivot]:
                    l = pivot + 1
                else:
                    r = pivot - 1
        return -1   
"""
33. Search in Rotated Sorted Array
Medium

3163

371

Favorite

Share
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
