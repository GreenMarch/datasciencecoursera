from heapq import heappush, heapreplace
class Solution:
    def minMeetingRooms(self, intervals):
        h = []
        for i in sorted(intervals):
            print(i,intervals)
            if h == [] or h[0] > i[0]:
                print("== or >", h, i[0])
                heappush(h, i[1])
                print("heap is", h)
            else:
                print("else", h[0], i[1])
                heapreplace(h, i[1])
                print("heap is", h)
        return len(h)

inputdata = [[0,30],[5,10],[15,20]]
print(Solution().minMeetingRooms(inputdata))

"""
253. Meeting Rooms II
Medium

2154

31

Add to List

Share
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
