class Solution:
    # pass
    def reverse(self, x):
        if x >= 2**31-1 or x <= -2**31: 
            return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[::-1]
            else:
                temp = strg[1:] 
                temp2 = temp[::-1] 
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: 
                return 0
            else: 
                return int(revst)
            
    # not pass
    def reverse(self, x: int) -> int:
        if x > 2**10:
            return 0
        elif x >= 0:
            return self.reverse_pos(x)
        else:
            return self.reverse_pos(x*-1)*-1
        
    def reverse_pos(self, x):
        x_str = str(x)
        new_str_list = []
        for i in range(len(x_str)):
            new_str_list.append(x_str[len(x_str) - i - 1])
        new_str = "".join(new_str_list)
        return int(new_str)
"""
7. Reverse Integer
Easy

2561

4007

Favorite

Share
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
