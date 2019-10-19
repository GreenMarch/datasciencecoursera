class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        h = []
        for i in sorted(intervals):
            if h == [] or h[0] > i[0]:
                heapq.heappush(h, i[1])
            else:
                heapq.heapreplace(h, i[1])
        return len(h)
