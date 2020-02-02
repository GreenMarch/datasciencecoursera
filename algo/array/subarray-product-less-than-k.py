class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        # left, right = 0, len(nums) - 1
        # while left <= right:

        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            print(nums[left:right + 1])
            ans += right - left + 1
        return ans


inputdata = [10, 5, 2, 6]
val = 100
print(Solution().numSubarrayProductLessThanK(inputdata, val))