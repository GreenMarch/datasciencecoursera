# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/discuss/469009/Python-simple-stack-O(n)-for-time-and-space
class Solution:
    def verifyPreorder(self, preorder):
        """
        :param preorder: : List[int]
        :return:  -> bool
        """

        chk, stack = None, []
        for n in preorder:
            print("n",n)
            while stack and n > stack[-1]:
                chk = stack.pop()
            if chk != None and n < chk:
                return False
            stack.append(n)
            print("stack",stack)
        return True

inputdata = [5,2,1,3,6]
res = Solution().verifyPreorder(inputdata)
print(res)
"""
255. Verify Preorder Sequence in Binary Search Tree
Medium

519

48

Add to List

Share
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
Follow up:
Could you do it using only constant space complexity?
"""