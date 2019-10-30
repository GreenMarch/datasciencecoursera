class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            print("check dict")
            print(d.get(sums-k,0))
            print("count: " + str(count))
            count += d.get(sums-k,0)
            print("count2: " + str(count))
            d[sums] = d.get(sums,0) + 1
        
        return(count)
        
            
    def subarraySum2(self, A, K):
        import collections
        count = collections.Counter()
        count[0] = 1
        ans = su = 0
        for x in A:
            su += x
            ans += count[su-K]
            count[su] += 1
        return ans
        
data = [1,1,1,1]
print("a")
Solution().subarraySum(data,3)

print("b")
Solution().subarraySum2(data,2)


#%%
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        
        return(count)
        
            
    def subarraySum2(self, A, K):
        import collections
        count = collections.Counter()
        count[0] = 1
        ans = su = 0
        for x in A:
            su += x
            ans += count[su-K]
            count[su] += 1
        return ans
        
data = [1,1,1]
print("a")
Solution().subarraySum(data,3)

print("b")
Solution().subarraySum2(data,3)
"""
560. Subarray Sum Equals K
Medium

2653

72

Favorite

Share
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
