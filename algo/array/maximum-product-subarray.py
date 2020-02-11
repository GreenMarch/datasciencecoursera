# p[i] stands for the largest product of all subarrays containing nums[i+1].
# n[i] stands for the smallest negative product of all subarrays containing nums[i+1], and I use None to represent the situation where no negative product exists.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = float('-inf')
        p, n = [0], [None]
        for i, x in enumerate(nums):
            if x > 0:
                p.append(p[-1] * x if p[-1] > 0 else x)
                n.append(n[-1] * x if n[-1] else None)
            elif x < 0:
                p.append(n[-1] * x if n[-1] else x)
                n.append(p[-2] * x if p[-2] > 0 else x)
            else:
                p.append(0)
                n.append(None)
            m = max(m, p[-1])
        return m


# Bonus:
# Share another beautiful solution found in the fastest code sample pool (slightly modified), the guy who came up with this one is a genius.
# Basically, the idea is to first (implicitly) split nums into subarrays with no zeros, then for each of the subarray if the number of negative numbers is even, the max is simply the product of the whole subarray, otherwise (if it is odd), the max must be the product of a subarray which has the largest even number of negative numbers, which is covered by either A or B.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        A, B = nums, nums[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i-1] or 1
            B[i] *= B[i-1] or 1
        return max(*A, *B)

"""

"""
152. Maximum Product Subarray
Medium

3123

133

Add to List

Share
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""