# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        import heapq
        self.small = []  # maxheap
        self.large = []  # minheap

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.small, -num)
            tmp = heapq.heappop(self.small)
            heapq.heappush(self.large, -tmp)
        else:
            heapq.heappush(self.large, num)
            tmp = heapq.heappop(self.large)
            heapq.heappush(self.small, -tmp)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return self.large[0]

"""
295. Find Median from Data Stream
Hard

1984

38

Add to List

Share
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""