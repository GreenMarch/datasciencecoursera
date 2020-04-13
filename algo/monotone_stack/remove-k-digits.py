class Solution:
    def removeKdigits(self, num, k):
        """
        :param num: str
        :param k: int
        :return: str
        """
        stk = []
        for n in num:
            while k > 0 and stk and stk[-1] > n:
                stk.pop()
                k -= 1
            if not stk and n == "0":
                continue
            else:
                stk.append(n)
        print(k, stk)
        while k > 0 and stk:
            stk.pop()
            k -= 1
        return "".join(stk) if stk else "0"

input_str = "1432219"
k = 3
print(Solution().removeKdigits(input_str, k))