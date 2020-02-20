class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast, slow = 0, 0
        while fast < len(nums):
            print(slow, fast)
            if nums[fast] == 0:
                # slow += 1
                fast += 1
                continue
                print(slow, fast)
            if slow != fast:
                nums[slow] = nums[fast]
                nums[fast] = 0
                print(slow, fast)
            slow += 1
            fast += 1

# public void moveZeroes(int[] nums) {
#     int readIndex = 0;
#     int writeIndex = 0;

#     while(readIndex < nums.length){
#         if(nums[readIndex] == 0){
#             readIndex++;
#             continue;
#         }

#         if(readIndex != writeIndex){
#             nums[writeIndex] = nums[readIndex];
#             nums[readIndex] = 0;
#         }
#         writeIndex++;
#         readIndex++;
#     }
# }

"""
283. Move Zeroes
Easy

2921

97

Add to List

Share
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""