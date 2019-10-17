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
