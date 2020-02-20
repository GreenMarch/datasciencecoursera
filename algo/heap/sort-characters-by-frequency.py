from collections import Counter
import heapq

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
"""


class Solution:
    def frequencySort(self, s):
        # letters = [char for char in s.split()]
        letters = list(s)
        count = Counter(letters)
        #         k = len(set(letters))
        #         res = heapq.nlargest(k, count.keys(), key=count.get)
        heap = [(val, ord('z') - ord(key)) for key, val in count.items()]
        heapq.heapify(heap)

        s = ''
        while len(heap) > 0:
            v, k = heapq.heappop(heap)
            k = chr(ord('z') - k)
            s = "".join([k for _ in range(v)]) + s

        return s

data = "tree"
print(Solution().frequencySort(data))

"""
        letters = [char for char in s.split()]
        print("letters",letters)
        count = Counter(letters)
        l = len(set(letters))
        return count.most_common(l)



		dic = {}
        result = ""

		# loop through each char, and add the count to the dic
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

		# sort the dic on values in reverse order
        sorted_dic = sorted(dic, key=dic.get, reverse=True)

		# loop through, and create final string
        for count in sorted_dic:
            result += count * (dic[count])

        return result
"""
