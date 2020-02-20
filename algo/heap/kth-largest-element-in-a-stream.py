from heapq import heappop, heappush, heapify, heappushpop
class KthLargest:

    def __init__(self, k, nums):
        self.heap = []
        self.k = k
        for i in nums:
            if len(self.heap) < k:
                heappush(self.heap, i)
            else:
                if i > self.heap[0]:
                    heappushpop(self.heap, i)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heappushpop(self.heap, val)
        return self.heap[0]

k = 3
arr = [4,5,8,2]
kthLargest = KthLargest(3, arr)
kthLargest.add(3)   #// returns 4
kthLargest.add(5)   #// returns 5
kthLargest.add(10)  #// returns 5
kthLargest.add(9)   #// returns 8
kthLargest.add(4)   #// returns 8