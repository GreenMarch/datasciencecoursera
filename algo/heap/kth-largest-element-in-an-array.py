import heapq
class Solution:
    def findKthLargest(self, nums, k):
        # nums.sort()
        # return nums[len(nums) - k]
        heap = nums
        heapq.heapify(heap)
        for i in range(len(nums) - k + 1):
            print("i", i)
            res = heapq.heappop(heap)
        return res

data = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(data, k))