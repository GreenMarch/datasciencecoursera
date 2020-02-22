class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        miss = (1 + len(nums)) * len(nums) // 2 - sum(set(nums))
        dup = sum(nums) + miss - (1 + len(nums)) * len(nums) // 2
        return [dup, miss]

        # n = len(nums)
        # s = n*(n+1)//2
        # miss = s - sum(set(nums))
        # duplicate = sum(nums) + miss - s
        # return [duplicate, miss]

        #         nums.sort()
        #         for i in range(len(nums)):
        #             if nums[i] != i + 1:
        #                 return [nums[i], i + 1]

        """
            seen = set()
            for i in range(len(nums) - 1, 0, -1):
                if nums[i] not in seen:
                    seen.add(nums[i])
                else:
                    print("i", i)
                    return [nums[i],int((nums[i + 2] + nums[i])/2)]

        elif len(nums) == 2:
            if nums[0] == nums[1] and nums[0] == 1:
                return [1,nums[0] + 1]
            elif nums[0] == nums[1] and nums[1] == 1:
                return [1,nums[1] + 1]
            elif nums[0] == nums[1]:
                return [max(nums),1]
        """


"""
645. Set Mismatch
Easy

532

274

Add to List

Share
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.


"""