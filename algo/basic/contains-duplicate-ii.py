class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :param nums: List[int]
        :param k: in
        :return: bool
        """
        max_diff = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i != j and nums[i] == nums[j]:
                    print("i j", i, j)
                    max_diff = max(max_diff, abs(i - j))
                    print(i, j, nums[i], nums[j], max_diff)
        return max_diff <= k


data = [1,0,1,1]
k = 1
print(Solution().containsNearbyDuplicate(data, k))