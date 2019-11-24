# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        from collections import deque
        if not root:
            return False
        queue = deque([root])
        seen = set()
        while queue:
            curr = queue.popleft()
            if curr.val in seen:
                return True
            else:
                seen.add(k - curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return False
"""
653. Two Sum IV - Input is a BST
Easy

1065

121

Favorite

Share
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

Complexity analysis

Time complexity: O(n)
where n is the number of nodes in the binary tree. The algorithm needs to visit every nodes in the binary search tree in the worst case.
Space complexity: O(n)
where n is the number of nodes in the binary tree.
"""
