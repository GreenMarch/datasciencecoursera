class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        print("A: " + str(A))
        S = -1
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] + A[j] < K:
                S = max(A[i] + A[j], S)
                i += 1
            else:
                j -= 1
        return S
    
"""
1099. Two Sum Less Than K
Easy

137

15

Favorite

Share
Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.
 

Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
"""
        
"""
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if len(A) < 2:
            return -1
        else:
            all_twosum = []
            for i in range(0, len(A) - 1):
                for j in range(i + 1, len(A)):
                    all_twosum.append(A[i] + A[j])
            good_list = [x for x in all_twosum if x < K]
            if len(good_list) < 1:
                return -1
            else:
                good_list.sort()
                return good_list[len(good_list) - 1]
"""
