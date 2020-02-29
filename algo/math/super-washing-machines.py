class Solution:
    # def findMinMoves(self, machines: List[int]) -> int:
    #     if sum(machines) % len(machines) != 0:
    #         return -1

    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        dress_total = sum(machines)
        if dress_total % n != 0:
            return -1

        dress_per_machine = dress_total // n
        for i in range(n):
            # Change the number of dresses in the machines to
            # the number of dresses to be removed from this machine
            # (could be negative)
            machines[i] -= dress_per_machine
        # curr_sum is a number of dresses to move at this point,
        # max_sum is a max number of dresses to move at this point or before,
        # m is number of dresses to move out from the current machine.
        curr_sum = res = 0
        for m in machines:
            curr_sum += m
            print("res, abs(curr_sum), m:", res, abs(curr_sum), m)
            res = max(res, abs(curr_sum), m)
        return res

data = [1,0,5]
print(Solution().findMinMoves(data))
