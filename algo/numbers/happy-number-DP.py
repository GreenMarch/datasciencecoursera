class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 7:
            return False
        l = len(str(n))
        nums = []
        for i in range(l):
            nums.append(int(str(n)[i]))

        sq_sum = 0
        for item in nums:

            sq_sum += item*item

        return self.isHappy(sq_sum)

'''
    202. Happy Number
Easy

1086

281

Favorite

Share
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''
