from collections import Counter
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        count = Counter(A)
        for num, freq in count.items():
            if freq != 1:
                return num
        # B = sorted(A)
        # print(B)
        # if B[len(A) // 2 - 1] == B[len(A) // 2 - 2]:
        #     return B[len(A) // 2 - 1]
        # else:
        #     return B[len(A) // 2]

"""
961. N-Repeated Element in Size 2N Array
Easy

338

200

Add to List

Share
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5
 

Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
Accepted
96,692
Submissions
132,490
"""