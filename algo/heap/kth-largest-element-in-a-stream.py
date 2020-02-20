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
print(kthLargest.add(3)) #// returns 4
print(kthLargest.add(5))   #// returns 5
print(kthLargest.add(10))  #// returns 5
print(kthLargest.add(9)) #// returns 8
print(kthLargest.add(4))   #// returns 8

"""
703. Kth Largest Element in a Stream
Easy

516

270

Add to List

Share
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.
"""