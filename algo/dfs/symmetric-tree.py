# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(t1, t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            else:
                return t1.val == t2.val and dfs(t1.left, t2.right) and dfs(t1.right, t2.left)
        return dfs(root, root)

"""
101. Symmetric Tree
Easy

3215

75

Add to List

Share
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.


"""