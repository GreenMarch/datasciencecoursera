class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        max_area = 0
        while start < end:
            print("(end - start): " + str((end - start)))
            print(str(height[start]))
            print(str(height[end]))
            max_area = max(max_area, (end - start) * min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_area
#         max_area = 0

#         for i in range(len(height)):
#             for j in range(i + 1, len(height)):
#                 max_area = max(max_area, min(height[i], height[j]) * (j - i))
#         return max_area          
        
"""
11. Container With Most Water
Medium

4177

484

Favorite

Share
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""
