from heapq import heappush, heapreplace
class Solution:
    def minMeetingRooms(self, intervals):
        h = []
        for i in sorted(intervals):
            if h == [] or h[0] > i[0]:
                heappush(h, i[1])
            else:
                heapreplace(h, i[1])
        return len(h)

inputdata = [[0,30],[5,10],[15,20]]
print(Solution().minMeetingRooms(inputdata))