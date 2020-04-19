class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)

        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            current_quotient = 1
            while (the_sum << 1) <= dividend:
                the_sum <<= 1
                current_quotient <<= 1
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient

        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))

    """
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        if dividend == MAX_INT and divisor == 1:
            return MAX_INT
        if dividend == MIN_INT and divisor == 1:
            return MIN_INT
        if dividend == MAX_INT and divisor == -1:
            return MIN_INT
        # We need to convert both numbers to negatives
        # for the reasons explained above.
        # Also, we count the number of negatives signs.
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        # Count how many times the divisor has to be
        # added to get the dividend. This is the quotient.
        quotient = 0
        while dividend - divisor <= 0:
            quotient -= 1
            dividend -= divisor

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive.
        return -quotient if negatives != 1 else quotient


#         i = 0
#         divisor_abs, dividend_abs = abs(divisor), abs(dividend)
#         while i * divisor_abs <= dividend_abs:
#             i += 1
#             print(i, dividend, divisor)
#         return (i - 1) if dividend*divisor > 0 else 1 - i

        """

"""
29. Divide Two Integers
Medium

1016

4788

Add to List

Share
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
"""