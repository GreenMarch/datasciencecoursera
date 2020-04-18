import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            if left ** 2 + right ** 2 > c:
                right -= 1
            elif left ** 2 + right ** 2 < c:
                left += 1
            else:
                return True
        return False
    #     def judgeSquareSum(self, c: int) -> bool:
    #         ub = int(sqrt(c))
    #         for a in range(ub + 1):
    #             b = c - a**2
    #             if self.binary_search(0, b, b):
    #                 return True
    #         return False

    #     def binary_search(self, s, e, n):
    #         if s > e:
    #             return False
    #         mid = s + (e - s) // 2
    #         if mid**2 == n:
    #             return True
    #         elif mid**2 > n:
    #             return self.binary_search(s, mid - 1, n)
    #         else:
    #             return self.binary_search(mid + 1, e, n)

"""
633. Sum of Square Numbers
Easy

461

293

Add to List

Share
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3
Output: False
"""