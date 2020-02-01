class Solution:
    def findUnsortedSubarray(self, nums):
        sortedNums = sorted(nums)
        start, end = -1, -1

        i = 0
        while (i < len(nums)):
            if nums[i] != sortedNums[i]:
                start = i
                break
            i += 1
        if start == -1:
            return 0  # already sorted

        i = len(nums) - 1
        while (i >= 0):
            if nums[i] != sortedNums[i]:
                end = i
                break
            i -= 1
        return end - start + 1
        # return nums[start:end + 1]


inputdata = [2, 6, 4, 8, 10, 9, 15]
Solution().findUnsortedSubarray(inputdata)