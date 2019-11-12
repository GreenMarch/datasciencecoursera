class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums.sort()
        if len(nums) % 2 == 1:
            idx = len(nums) // 2
        else:
            idx = len(nums) // 2 - 1
        return target == nums[idx]
