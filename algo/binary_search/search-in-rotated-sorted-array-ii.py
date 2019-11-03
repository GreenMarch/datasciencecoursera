class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            pivot = l + (r - l) // 2
            if nums[pivot] == target:
                return True
            while l < pivot and nums[l] == nums[pivot]: # tricky part
                l += 1
            if nums[pivot] >= nums[l]:
                if target >= nums[l] and target < nums[pivot]:
                    r = pivot - 1 
                else:
                    l = pivot + 1
            else:
                if target <= nums[r] and target > nums[pivot]:
                    l = pivot + 1
                else:
                    r = pivot - 1 
        return False
    
#     def search(self, nums, target):
#         l, r = 0, len(nums)-1
#         while l <= r:
#             mid = l + (r-l)//2
#             if nums[mid] == target:
#                 return True
#             while l < mid and nums[l] == nums[mid]: # tricky part
#                 l += 1
#             # the first half is ordered
#             if nums[l] <= nums[mid]:
#                 # target is in the first half
#                 if nums[l] <= target < nums[mid]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#             # the second half is ordered
#             else:
#                 # target is in the second half
#                 if nums[mid] < target <= nums[r]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#         return False
                    
                
            
"""
81. Search in Rotated Sorted Array II
Medium

855

362

Favorite

Share
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""
