class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out = [None]*len(nums)
        out[0] = nums[0]
        for i in range(1, len(nums)):
            out[i] = max(out[i - 1] + nums[i], nums[i])
        return max(out)
