class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        def is_consecutive(n):
            for i in range(1, len(n) - 1):
                if n[i] != n[i - 1] + 1:
                    return False
            return True

        res = False
        print("res:", res)
        for i in range(1, len(nums) - 1):
            if not is_consecutive(nums[:i]) or not is_consecutive(nums[i:]) or not (len(nums[:i]) >= 3) or not (
                    len(nums[i:]) >= 3):
                continue
            else:
                return True
        return False




