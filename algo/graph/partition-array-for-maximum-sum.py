class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        # 0) Initialization
        #    best_a is used to keep past computation result
        #    best_a[i] is to keep local optimal result of A[0:i-1]
        best_a = [0] * len(A)
        best_a[0] = A[0]

        # 1) Iteratively fill the best_a with local optimal result
        #    best_a[0] = A[0]
        #    best_a[1] = max(best_a[0] + A[1], max(A[0:2]) * 2)
        #    best_a[2] = max(best_a[1] + A[2], best_a[0] + max(A[1:3]) * 2, max(A[0:3]) * 3)
        #    ...
        #    best_a[n] = max(best_a[n-1] + A[n], best_a[n-2] + max(A[n-1:n+1]) * 2, ..., max(A[n-K+1:n+1]) * K)
        for i in range(1, len(A)):
            max_v = 0
            for j in range(i, max(-1, i-K), -1):
                sa = A[j:i+1]
                v = best_a[j-1] + max(sa) * len(sa)
                if v > max_v:
                    max_v = v

            best_a[i] = max_v

        # 3) The global optimal result is kept in last element
        return best_a[-1]


"""
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n=len(A)
        dp=[0]*(n+1)
        for i in range(1,n+1):
            num=float('-inf')
            print("i,K",i,K)
            for j in range(1,min(i,K)+1):
                print(i,j,A[i-j],num,dp[i],dp[i-j]+num*j)
                num=max(num,A[i-j])
                dp[i]=max(dp[i],dp[i-j]+num*j)   
        return dp[n]
"""

"""
1043. Partition Array for Maximum Sum
Medium

440

61

Add to List

Share
Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.  After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

 

Example 1:

Input: A = [1,15,7,9,2,5,10], K = 3
Output: 84
Explanation: A becomes [15,15,15,9,10,10,10]
 

Note:

1 <= K <= A.length <= 500
0 <= A[i] <= 10^6

"""