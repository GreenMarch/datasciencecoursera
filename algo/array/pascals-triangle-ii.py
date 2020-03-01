class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * rowIndex
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            row[0] = 1
        for i in range(1, rowIndex + 1):
            last = 1
            for j in range(1, i):
                row[j], last = last + row[j], row[j]
        row.append(1)
        return row

# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         row = [1]*(rowIndex+1)
#         for i in range(1, rowIndex+1):
#             last = 1
#             for j in range(1,i):
#                 row[j], last = last + row[j], row[j]
#         return row

"""
119. Pascal's Triangle II
Easy

646

188

Add to List

Share
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""