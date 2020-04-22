class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for a, b in intervals:
            if b <= toBeRemoved[0] or a >= toBeRemoved[1]:  # out of range
                res.append([a, b])
            elif a < toBeRemoved[0] < b <= toBeRemoved[1]:  # intersect in the front
                res.append([a, toBeRemoved[0]])
            elif toBeRemoved[0] <= a < toBeRemoved[1] < b:  # intersect on the back
                res.append([toBeRemoved[1], b])
            elif a < toBeRemoved[0] and b > toBeRemoved[1]:  # interval is bigger than toBeRemoved
                res.append([a, toBeRemoved[0]])
                res.append([toBeRemoved[1], b])
        return res

"""
1272. Remove Interval
Medium

68

6

Add to List

Share
Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the set of real numbers x such that a <= x < b.

We remove the intersections between any interval in intervals and the interval toBeRemoved.

Return a sorted list of intervals after all such removals.

 

Example 1:

Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]
Example 2:

Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]
 

Constraints:

1 <= intervals.length <= 10^4
-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9
"""