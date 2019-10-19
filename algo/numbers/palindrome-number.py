class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            orig = x
            back_x = 0
            while x > 0:
                back_x = (back_x * 10) + (x % 10)
                x = x // 10
            return orig == back_x
