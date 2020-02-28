from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        return len(list(count.values())) == len(set(count.values()))
