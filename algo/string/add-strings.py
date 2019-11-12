class Solution:
    
    def addStrings(self, num1: str, num2: str) -> str:
        N1, N2 , carry = len(num1), len(num2) , 0
        i , j = N1 -1 , N2 - 1
        res = []
        while i  >= 0  or j >=  0:
            a =   0 if i < 0 else int(num1[i]) 
            b =   0 if j < 0 else int(num2[j])            
            tmp = a + b + carry
            res.append(str(tmp % 10))
            carry = tmp // 10
            i -= 1
            j -= 1        
        res.reverse()
        res_str = ''.join(res)
        return str(carry) + res_str if carry else res_str
    
    def addStrings2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        rst = ''
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        
        diff = len(num2) - len(num1)
        num1 = '0' * diff + num1
        
        carry = 0
        for i, j in zip(num1[::-1], num2[::-1]):
            cur = ord(i) + ord(j) - 2 * ord('0') + carry
            carry = cur // 10
            rst = str(cur % 10) + rst
        return '1' + rst if carry else rst
""" 
data = "10"
data2 = "100"
Solution().addStrings2(data, data2)

415. Add Strings
Easy

544

184

Favorite

Share
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""
