# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root)
    
    def helper(self, node, lower = float('-inf'), upper = float('inf')):
        if not node:
            return True

        val = node.val
        if val <= lower or val >= upper:
            return False

        if not self.helper(node.right, val, upper):
            return False
        if not self.helper(node.left, lower, val):
            return False
        return True
    
'''
98. Validate Binary Search Tree
Medium

2507

367

Favorite

Share
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
