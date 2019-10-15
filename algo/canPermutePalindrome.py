class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = {}
        for item in s:
            dic[item] = dic.get(item, 0) + 1
        count1 = 0
        for val in dic.values():
            if val % 2 == 1:
                count1 += 1
            if count1 > 1:
                return False
        return True
