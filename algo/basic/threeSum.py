class Solution:
    def threeSum(self, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        nums.sort()
        out = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    out.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return list(out)
    
    

class Solution:
    def threeSum(self, nums):
        out = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        out_temp = [nums[i], nums[j], nums[k]]
                        out_temp.sort()
                        if out_temp not in out:
                            out.append(out_temp)
        return out
'''
15. 3Sum
Medium

4724

561

Favorite

Share
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
