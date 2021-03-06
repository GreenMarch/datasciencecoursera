# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs(root):
            if root is None:
                return 'null'
            tmp = str(root.val) + ','+ dfs(root.left) + ','+  dfs(root.right)
            return ','+tmp+','
        return dfs(s).find(dfs(t)) >= 0
    
    
#     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#         if not s:
#             return False
#         if self.isSametree(s, t):
#             return True
#         else:
#             return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
#     def isSametree(self, i: TreeNode, j: TreeNode) -> bool:
#         if i and j:
#             return i.val == j.val and self.isSametree(i.left, j.left) and self.isSametree(i.right, j.right)

'''
572. Subtree of Another Tree
Easy

1452

55

Favorite

Share
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''
