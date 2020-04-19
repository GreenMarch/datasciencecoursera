class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1 = f2 = 0
        for x in reversed(cost):
            print("x, f1, f2,", x, f1, f2)
            f1, f2 = x + min(f1, f2), f1
            print("x, f1, f2 after,", x, f1, f2)
        return min(f1, f2)


"""
746. Min Cost Climbing Stairs
Easy

1692

386

Add to List

Share
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""