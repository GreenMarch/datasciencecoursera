class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        n_minus_1 = 2
        n_minus_2 = 1
        all_ways = 0
        for i in range(2, n):
            all_ways = n_minus_1 + n_minus_2
            n_minus_2 = n_minus_1
            n_minus_1 = all_ways

        return all_ways
"""
70. Climbing Stairs
Easy

2828

98

Favorite

Share
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
