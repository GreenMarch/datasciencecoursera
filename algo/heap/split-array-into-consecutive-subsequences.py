import collections
import heapq

class Solution:

    def isPossible(self, nums):
        saved = collections.defaultdict(
            list)  # this map "saved" stores a heap for the sequence lengh stopping at each num
        # print("saved", saved.keys, saved.values)
        for num in nums:
            last = saved[num - 1]  # last is a heap stopping at num-1
            # print("num",num,"last", last)
            # if not last:
            #     l = 0
            # else:
            #     heapq.heappop(last)
            l = 0 if not last else heapq.heappop(last)  # the minimum length stopping at num-1
            # print("l",l,"last", last)
            current = saved[num]
            heapq.heappush(current, l + 1)
        for value in saved.values():
            for v in value:
                if v < 3:
                    return False
        return True


"""
    def isPossible(self, nums: List[int]) -> bool:    
        def is_consecutive(n):
            for i in range(1, len(n) - 1):
                if n[i] != n[i - 1] + 1:
                    return False
            return True

        res = False

        for i in range(1,len(nums) - 1):

            if not is_consecutive(nums[:i]) or not is_consecutive(nums[i:]) or not (len(nums[:i]) >= 3) or not (len(nums[i:]) >= 3):

                continue
            else:
                return True
        return False


#         print("res:",res)
#         return res

"""

"""
659. Split Array into Consecutive Subsequences
Medium

796

306

Add to List

Share
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

 

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:

Input: [1,2,3,4,4,5]
Output: False
 

Constraints:

1 <= nums.length <= 10000
"""