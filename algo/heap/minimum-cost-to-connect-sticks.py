import heapq
class Solution:
    def connectSticks(self, sticks):
        """
        :param sticks: List[int]
        :return: int
        """
        res = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            c = heapq.heappop(sticks)+heapq.heappop(sticks)
            print(c, res)
            res += c
            heapq.heappush(sticks,c)
        return res

"""
1167. Minimum Cost to Connect Sticks
Medium

195

57

Add to List

Share
You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

 

Example 1:

Input: sticks = [2,4,3]
Output: 14
Example 2:

Input: sticks = [1,8,3,5]
Output: 30
 

Constraints:

1 <= sticks.length <= 10^4
1 <= sticks[i] <= 10^4
"""