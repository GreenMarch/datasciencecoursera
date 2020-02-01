class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        out = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                out += 1
        return out
