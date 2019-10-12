class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        out_temp = [nums[i], nums[j], nums[k]]
                        if out_temp not in out:
                            out.append(out_temp)
        return set(out)
