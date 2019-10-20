class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while 0 in nums:
            counter = 0
            for i, value in enumerate(nums):
                if value == 0:
                    del nums[i]
                    counter += 1
            print(counter)
        for j in range(counter):
            nums.append(0)
        

'''283. Move Zeroes
Easy

2456

90

Favorite

Share
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.'''
