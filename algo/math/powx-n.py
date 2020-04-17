class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = n*-1
        ans = 1
        while n :
            if n % 2:
                ans = x * ans
                n -= 1
            else:
                print(x, n)
                x = x * x
                n = n // 2
        return ans

"""
50. Pow(x, n)
Medium

1252

2771

Add to List

Share
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""