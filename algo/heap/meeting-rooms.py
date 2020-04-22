from heapq import nlargest, heappush
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        h = []
        for i in sorted(intervals):
            if h == [] or nlargest(1, h)[0] <= i[0]:
                heappush(h, i[1])
        if len(h) == len(intervals):
            return True
        else:
            return False

"""
252. Meeting Rooms
Easy

523

34

Add to List

Share
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""