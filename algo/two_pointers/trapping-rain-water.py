class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        volume = 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[left], height[right]
        while left < right:
            l_max, r_max = max(height[left], l_max), max(height[right], r_max)
            if l_max <= r_max:
                volume += l_max - height[left]
                left += 1
            else:
                volume += r_max - height[right]
                right -= 1
        return volume
    
#         """
#         https://www.youtube.com/watch?v=ZI2z5pq0TqA
#         """
#         if not height: return 0
        
#         l, r = 0, len(height) - 1
#         leftMax, rightMax = height[l], height[r]
#         res = 0
        
#         while l < r:
#             if leftMax < rightMax:
#                 l += 1
#                 leftMax = max(leftMax, height[l])
#                 res += leftMax - height[l]
#             else:
#                 r -= 1
#                 rightMax = max(rightMax, height[r])
#                 res += rightMax - height[r]
#         return res

"""
42. Trapping Rain Water
Hard

4782

83

Favorite

Share
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
