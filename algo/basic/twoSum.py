class Solution:
    def twoSum_h(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if target - nums[i] not in d:
                d[nums[i]] = i
            else:
                return [d[target - nums[i]],i]

"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
"""

nums = [2, 7, 11, 15]
target = 18
print(Solution().twoSum_h(nums, target))