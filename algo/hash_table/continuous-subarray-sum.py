class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        my_hashmap = {0: -1}
        su = 0
        for idx, num in enumerate(nums):
            su += num
            if k != 0:
                su = su % k
            if su in my_hashmap:
                if idx  - my_hashmap[su] > 1:
                    return True
            else:
                my_hashmap[su] = idx
        return False
"""
523. Continuous Subarray Sum
Medium

877

1203

Favorite

Share
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Note:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""
