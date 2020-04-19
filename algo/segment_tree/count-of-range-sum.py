# class Solution:
#     def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:

# # Approach 2 : Prefix-sum + SegmentTree
# Inspired by Java SegmentTree Solution, 36ms
# You can see, it was vsery similay to approach 1, SegmentTree is very useful for processing range queries, utilize SegmentTree to make query time from O(upper-lower+1) to O(logn)

class SegmentTreeNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.left = None
        self.right = None
        self.cnt = 0


class Solution:
    def _bulid(self, left, right):
        root = SegmentTreeNode(self.cumsum[left], self.cumsum[right])
        if left == right:
            return root

        mid = (left + right) // 2
        root.left = self._bulid(left, mid)
        root.right = self._bulid(mid + 1, right)
        return root

    def _update(self, root, val):
        if not root:
            return
        if root.low <= val <= root.high:
            root.cnt += 1
            self._update(root.left, val)
            self._update(root.right, val)

    def _query(self, root, lower, upper):
        if lower <= root.low and root.high <= upper:
            return root.cnt
        if upper < root.low or root.high < lower:
            return 0
        return self._query(root.left, lower, upper) + self._query(root.right, lower, upper)

    # prefix-sum + SegmentTree | O(nlogn)
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cumsum = [0]
        for n in nums:
            cumsum.append(cumsum[-1] + n)

        self.cumsum = sorted(list(set(cumsum)))  # need sorted
        root = self._bulid(0, len(self.cumsum) - 1)

        res = 0
        for csum in cumsum:
            res += self._query(root, csum - upper, csum - lower)
            self._update(root, csum)
        return res

"""
327. Count of Range Sum
Hard

635

79

Add to List

Share
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
"""