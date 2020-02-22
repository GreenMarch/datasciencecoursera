class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach #2 HashSet [Accepted]
        num_set = set(nums)
        n = len(nums) + 1
        for i in range(n):
            if i not in num_set:
                return i
        
        """
        # Approach #4 Gauss' Formula 
        return len(nums)*(len(nums) + 1) // 2 - sum(nums)
        # Approach #1 Sorting [Accepted]
        nums.sort()
        
        if nums[-1] != len(nums):
            return len(nums)
        
        elif nums[0] != 0:
            return 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                return nums[i - 1] + 1
        """
        
"""
268. Missing Number
Easy

1154

1567

Favorite

Share
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
