from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: List[int]
        """
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

        # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = Counter(nums)
    #     return list(zip(*count.most_common(k)))[0]

inputlist = [1,2,2,3,3,3]
print(Solution().topKFrequent(inputlist, 2))