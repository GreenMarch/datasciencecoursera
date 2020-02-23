class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []  # indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            print("i", i)
            while stack and T[i] >= T[stack[-1]]:
                print("stack", stack[-1])
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
            print("full stack", stack, "full res", ans)
        return ans

        # res = [0]*len(T)
        # i = 0
        #     for j in range(i, len(T)):
        #         if T[i] < T[j]:
        #             res[i] = j - i
        #             break
        #     i += 1
        # return res

#         res = [0]*len(T)
#         i = 0
#         while i <= len(T):
#             warmer_days = []
#             for j in range(i, len(T)):
#                 if T[i] < T[j]:
#                     warmer_days.append(j - i)
#                     res[i] = min(warmer_days)

#             i += 1
#         return res


"""
739. Daily Temperatures
Medium

2081

66

Add to List

Share
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

Accepted
121,869
Submissions
196,732
"""