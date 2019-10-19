class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0 or k == len(nums): 
            nums = nums
        # elif k == len(nums) - 1:
        #     last = nums[-1]
        #     print("last" + str(last))
        #     nums_exclude_last = nums[:k]
        #     print("nums_exclude_last" + str(nums_exclude_last))
        #     nums[0] = last
        #     nums[1:] = nums_exclude_last
        #     # nums = last + nums_exclude_last
        #     print(nums)
        else:
            right = nums[-k:]
            left = nums[:-k]
            nums[:-k] = right
            nums[k:] = left
