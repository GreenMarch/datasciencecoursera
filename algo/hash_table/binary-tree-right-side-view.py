# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            left = self.rightSideView(root.left)
            right = self.rightSideView(root.right)
            if len(right) >= len(left):
                return [root.val] + right
            else:
                return [root.val] + right + left[len(right):]


"""
199. Binary Tree Right Side View
Medium

1655

87

Add to List

Share
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""