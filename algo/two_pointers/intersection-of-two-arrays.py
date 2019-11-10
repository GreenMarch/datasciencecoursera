class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        d = {}
        
        for i in nums1:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        out = []
        
        for j in nums2:
            if j in d:
                out.append(j)
            else:
                continue
                
        return set(out)
        
"""
349. Intersection of Two Arrays
Easy

502

920

Favorite

Share
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""
