class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0 or k == len(nums): 
            nums = nums
        # elif k == len(nums) - 1:
        #     last = nums[-1]
        #     print("last" + str(last))
        #     nums_exclude_last = nums[:k]
        #     print("nums_exclude_last" + str(nums_exclude_last))
        #     nums[0] = last
        #     nums[1:] = nums_exclude_last
        #     # nums = last + nums_exclude_last
        #     print(nums)
        else:
            right = nums[-k:]
            left = nums[:-k]
            nums[:-k] = right
            nums[k:] = left

"""
189. Rotate Array
Easy

2085

730

Add to List

Share
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""