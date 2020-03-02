import heapq
class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        """
        :param A: List[int]
        :param K: int
        :return: List[int]
        """
        # val = [(A[0] / float(A[i]), 0, i) for i in range(len(A) - 1, 0, -1)]

        # Note - this solution may TLE.
        val = []
        for i in range(len(A)):
            val.append((A[0] / float(A[i]), 0, i))
        heapq.heapify(val)
        while K > 1:
            frac, i, j = heapq.heappop(val)
            i += 1
            if i < j:
                heapq.heappush(val, (A[i] / float(A[j]), i, j))
            K -= 1
        return A[val[0][1]], A[val[0][2]]

"""
786. K-th Smallest Prime Fraction
Hard

305

17

Add to List

Share
A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.

What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.

Examples:
Input: A = [1, 2, 3, 5], K = 3
Output: [2, 5]
Explanation:
The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5.

Input: A = [1, 7], K = 1
Output: [1, 7]
Note:

A will have length between 2 and 2000.
Each A[i] will be between 1 and 30000.
K will be between 1 and A.length * (A.length - 1) / 2.
"""
