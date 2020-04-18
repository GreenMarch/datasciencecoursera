class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 1:
            return True
        left, right = 0, num // 2
        while left <= right:
            pivot = left + (right - left) // 2
            pivot_square = pivot ** 2
            if pivot_square == num:
                return True
            elif pivot_square < num:
                left = pivot + 1
            else:
                right = pivot - 1
        return False


"""
367. Valid Perfect Square
Easy

647

137

Add to List

Share
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""