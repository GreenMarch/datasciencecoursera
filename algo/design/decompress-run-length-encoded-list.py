class Solution:
    def decompressRLElist(self, nums):
        out = []
        for i in range(0, len(nums), 2):
            out.extend(nums[i]*[nums[i+1]])
        return out

input = [1,2,3,4]
print(Solution().decompressRLElist(input))