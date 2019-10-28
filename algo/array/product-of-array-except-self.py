class Solution:
    def productExceptSelf(self, nums):
        L = [0]*len(nums)
        R = [0]*len(nums)
        answer = [0]*len(nums)
        
        L[0] = 1
        for i in range(1, len(nums)):
            L[i] = nums[i - 1] * L[i - 1]
            
        R[len(nums) - 1] = 1
        for i in reversed(range(len(nums) - 1)):
            R[i] = nums[i + 1] * R[i + 1]
            
        for i in range(len(nums)):
            answer[i] = L[i] * R[i]
        return answer
"""
238. Product of Array Except Self
Medium

2954

255

Favorite

Share
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
