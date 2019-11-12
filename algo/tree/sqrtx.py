class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l = 2
        r = x
        while l <= r:
            pivot = l + (r - l) // 2
            if pivot**2 > x:
                r = pivot - 1
            else:
                l = pivot + 1
        return r

    
    """
Complexity Analysis

Time complexity : O(logN).

Space complexity : O(1).

"""
