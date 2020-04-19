# Binary Indexed Tree allows to query sums of the values of the list over any single range of indices in O(log n)
# by paying O(log n) price for any update and retrieval of value of nodes
class BinaryIndexedTree:
    def __init__(self, max_size):  # n = max_size
        self.size = max_size + 1
        self.tree = [0] * self.size

    def add_to_value_at(self, index, value):  # add to value at index starting from 0 O(log n)
        i = index + 1  # in tree it's from 1
        # update binary indexed tree
        while i < self.size:
            self.tree[i] += value
            i += i & -i

    def get_sum(self, to_index, from_index=0):  # return sum of all values in the range [from_index, to_index] O(log n)
        if from_index <= 0:
            i = to_index + 1  # in tree the index runs from 1
            res = 0
            while i:  # sum all tree values from 1 to i
                res += self.tree[i]
                i -= i & - i
            return res
        else:
            return self.get_sum(to_index) - self.get_sum(from_index - 1)

    def get_value(self, index):  # O(log n), not used in this problem, can be made O(1) using O(n) space
        return self.get_sum(to_index, to_index)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nsort = sorted(nums)
        # indices of unique values sorted
        nsort = [n for i, n in enumerate(nsort) if i == 0 or nsort[i - 1] != n]
        tree = BinaryIndexedTree(len(nsort))
        res = [0] * len(nums)
        # Iterate from the end of nums, finding smaller values for each n among already considered values
        for k, n in enumerate(reversed(nums)):
            # find index
            i = bisect.bisect_left(nsort, n)
            tree.add_to_value_at(i, 1)  # we have new/another occurence of index i, recording/adding it
            res[len(nums) - k - 1] = tree.get_sum(
                i - 1)  # get the sum over all recorded indices 0..i-1, because these values are less than nums[i]
        return res

"""
315. Count of Smaller Numbers After Self
Hard

1947

73

Add to List

Share
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""