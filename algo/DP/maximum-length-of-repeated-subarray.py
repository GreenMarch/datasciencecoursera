from collections import defaultdict


class Solution:
    # DP
    def findLength(self, A: List[int], B: List[int]) -> int:
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
        return max(max(row) for row in memo)

    # Brute Force with Initial Character Map [Time Limit Exceeded]
    # def findLength(self, A: List[int], B: List[int]) -> int:
    #     res = 0
    #     Bstarts = defaultdict(list)
    #     for j, y in enumerate(B):
    #         Bstarts[y].append(j)
    #         print(j, y, Bstarts[y])
    #     for i, x in enumerate(A):
    #         for j in Bstarts[x]:
    #             k = 0
    #             while i + k < len(A) and j + k < len(B) and A[i + k] == B[j + k]:
    #                 k += 1
    #             res = max(res, k)
    #     return res

"""
718. Maximum Length of Repeated Subarray
Medium

947

40

Add to List

Share
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
 

Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

"""