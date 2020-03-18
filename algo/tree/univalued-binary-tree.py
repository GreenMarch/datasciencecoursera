class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        left_correct = (not root.left) or (self.isUnivalTree(root.left) and root.val == root.left.val)
        right_correct = (not root.right) or (self.isUnivalTree(root.right) and root.val == root.right.val)
        return left_correct and right_correct

"""
data = [1, 1, 1, 1, 1, null, 1]
965. Univalued Binary Tree
Easy

363

39

Add to List

Share
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

 

Example 1:


Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: [2,2,2,5,2]
Output: false
"""





