from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        curr_level = max_level = 1
        max_sum = float('-inf')
        curr_sum = 0

        marker = None
        queue = deque([root, marker])

        while len(queue) > 1:
            x = queue.popleft()
            # continue current level
            if x != marker:
                curr_sum += x.val
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            # end of current level, go to the next level
            else:
                if curr_sum > max_sum:
                    max_sum, max_level = curr_sum, curr_level
                curr_sum = 0
                curr_level += 1
                queue.append(marker)

        return max_level

"""
1161. Maximum Level Sum of a Binary Tree
Medium

234

15

Add to List

Share
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

 

Example 1:



Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
 

Note:

The number of nodes in the given tree is between 1 and 10^4.
-10^5 <= node.val <= 10^5
"""