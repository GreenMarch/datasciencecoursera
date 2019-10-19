class Solution:
    def threeSum(self, nums):
        out = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        out_temp = [nums[i], nums[j], nums[k]]
                        out_temp.sort()
                        if out_temp not in out:
                            out.append(out_temp)
        return out
