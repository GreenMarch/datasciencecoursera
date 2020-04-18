class Solution:
    def closestDivisors(self, num: int) -> List[int]:

        def d(p):
            for i in range(int(p ** (1 / 2)), 0, -1):
                if (p % i) == 0:
                    return [i, p // i]

        return min(d(num + 1), d(num + 2), key=lambda k: abs(k[0] - k[1]))

    # class Solution:
#     def closestDivisors(self, num: int) -> List[int]:
#         target_1 = num + 1
#         target_2 = num + 2
#         t_list = [target_2, target_1]
#         print("t_list", t_list)
#         for t in t_list:
#             print("t", t)
#             # left, right = 0, t // 2
#             # pivot = left + (right - left) // 2
#             sqrt = int(math.sqrt(t))
#             # if left * right
#             left, right = sqrt, sqrt
#             while left >= 0 and right < num:
#                 print(left, right,t)
#                 if left*right == t:
#                     return [left, right]
#                 elif left*right > t:
#                     left -= 1
#                 else: right += 1
